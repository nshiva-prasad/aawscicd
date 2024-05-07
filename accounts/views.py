from django.views.generic import View, FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import CustomUserCreationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm, OTPLoginForm, OTPVerifyForm
from .models import CustomUser
from .tasks import send_verification_email, send_forgot_password_email, send_password_updated_email, send_otp_via_email
from django.urls import reverse
from django.db.models import Q
from datetime import datetime
import random


import logging

logger = logging.getLogger(__name__)


class RegisterPageView(View):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone')
            try:
                user = form.save()
                SendVerificationEmailView.send_verification_email_to_user(request, user)
                messages.success(request, "Verification email has been sent. Please check your email.")
                return redirect('login')
            except IntegrityError as e:
                messages.error(request, "Email or Phone number is already in use.")
        return render(request, self.template_name, {'form': form})


class LoginPageView(View):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        error_message = ""
        return render(request, self.template_name, {'form': form, 'error_message': error_message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email_or_phone = form.cleaned_data.get('email_or_phone')
            password = form.cleaned_data.get('password')
            print(email_or_phone, password)
            user = authenticate(request, email_or_phone=email_or_phone, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Invalid Email/Phone Number or Password. Try again."
                return render(request, self.template_name, {'form': form, 'error_message': error_message})
        else:
            error_message = "Please fill the form."
            return render(request, self.template_name, {'form': form, 'error_message': error_message})
        return render(request, self.template_name, {'form': form})


# class HomePageView(View):
#     template_name = 'accounts/home.html'

#     def get(self, request):
#         return render(request, self.template_name)

class LogoutPageView(View):

    def get(self, request):
        logout(request)
        return redirect('home')


class SendVerificationEmailView(View):
    @staticmethod
    def send_verification_email_to_user(request, user):

        token = default_token_generator.make_token(user)
        verification_url = f"{request.scheme}://{request.get_host()}/verify-email/{urlsafe_base64_encode(force_bytes(user.pk))}/{token}/"
        send_verification_email.delay(user.email, verification_url)


class VerifyEmailView(View):

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.email_verified = True
            user.save()
            messages.success(
                request, "Your email has been verified successfully.")
            return redirect('login')
        else:
            messages.error(request, "Invalid verification link.")
            return redirect('login')


class ForgotPasswordFormView(FormView):
    template_name = 'accounts/forgot_password.html'
    form_class = ForgotPasswordForm

    def form_valid(self, form):
        email_or_phone = form.cleaned_data.get('email_or_phone')
        user = CustomUser.objects.filter(Q(email=email_or_phone) | Q(phone=email_or_phone)).first()
        if user is not None:
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            password_reset_url = self.request.build_absolute_uri(
                reverse('reset_password_confirm', kwargs={
                        'uidb64': uidb64, 'token': token})
            )
            send_forgot_password_email.delay(user.email, password_reset_url)

            messages.success(self.request, "Password reset email has been sent successfully.")
        else:
            messages.success(self.request, "Password reset email has been sent successfully.")
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class ResetPasswordConfirmView(FormView):
    template_name = 'accounts/reset_password.html'
    form_class = ResetPasswordForm

    def form_valid(self, form):
        new_password = form.cleaned_data['new_password1']
        uidb64 = self.kwargs['uidb64']
        token = self.kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            print("user email is", user.email)
            send_password_updated_email.delay(user.email)
            user.set_password(new_password)
            user.save()
            messages.success(self.request, "Your password has been reset successfully.")
            return super().form_valid(form)
        else:
            messages.error(self.request, "The password reset link is invalid.")
            return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return reverse('login') 

class SendOTPView(View):
    template_name = 'accounts/otp_login.html'
    form_class = OTPLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        email_or_phone = self.kwargs.get('email_or_phone')
        form = self.form_class(request.POST)
        if form.is_valid():
            email_or_phone = form.cleaned_data.get('email_or_phone')
            user = CustomUser.objects.filter(Q(email=email_or_phone) | Q(phone=email_or_phone)).first()
            otp_code = random.randint(100000, 999999)
            request.session['otp_code'] = otp_code
            request.session['otp_email_or_phone'] = email_or_phone
            otp_sent_timestamp = datetime.now().timestamp()
            request.session['otp_sent_timestamp'] = otp_sent_timestamp
            if user.email:
                send_otp_via_email.delay(user.email, otp_code)
            messages.success(
                self.request, "OTP has been successfully sent your registered email.")
            return redirect(reverse('otp_verify', kwargs={'email_or_phone': email_or_phone}))
        return render(request, self.template_name, {'form': form})

class ResendOTPView(View):
    def get(self, request, email_or_phone):
        user = CustomUser.objects.filter(Q(email=email_or_phone) | Q(phone=email_or_phone)).first()
        otp_code = random.randint(100000, 999999)
        request.session['otp_code'] = otp_code
        request.session['otp_email_or_phone'] = email_or_phone
        otp_sent_timestamp = datetime.now().timestamp()
        request.session['otp_sent_timestamp'] = otp_sent_timestamp
        if user.email:
            send_otp_via_email.delay(user.email, otp_code)
        messages.success(request, "OTP resent successfully. Please use the latest OTP.")
        return redirect(reverse('otp_verify', kwargs={'email_or_phone': email_or_phone}))    

class OTPVerifyView(View):
    template_name = 'accounts/otp_verify.html'
    form_class = OTPVerifyForm

    def get(self, request, email_or_phone):
        form = self.form_class(initial={'email_or_phone': email_or_phone})
        return render(request, self.template_name, {'form': form, 'email_or_phone': email_or_phone})

    def post(self, request, email_or_phone):
        otp_code = request.POST.get('otp_code')
        if 'otp_code' in request.session:
            if request.session['otp_code'] == int(otp_code):
                otp_sent_time = request.session.get('otp_sent_timestamp')
                otp_sent_datetime = datetime.fromtimestamp(otp_sent_time)
                if otp_sent_time and (datetime.now() - otp_sent_datetime).seconds <= 600:
                    user = CustomUser.objects.filter(Q(email=email_or_phone) | Q(phone=email_or_phone)).first()
                    if user:
                        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                        return redirect('home')
                    else:
                        messages.error(request, "User not found.")
                else:
                    messages.error(request, "OTP has expired. Please try again.")
            else:
                messages.error(request, "Invalid OTP. Please try again.")
        else:
            messages.error(request, "OTP session expired. Please try again.")
        return render(request, self.template_name, {'form': self.form_class(), 'email_or_phone': email_or_phone})
    
    