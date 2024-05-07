from django.urls import path
from .views import RegisterPageView,LoginPageView, LogoutPageView, VerifyEmailView, SendVerificationEmailView, ForgotPasswordFormView, ResetPasswordConfirmView, SendOTPView, OTPVerifyView, ResendOTPView


urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('verify-email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('send-verification-email/', SendVerificationEmailView.as_view(), name='send_verification_email'),
    path('forgot-password/', ForgotPasswordFormView.as_view(), name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
    path('request-otp/', SendOTPView.as_view(), name='otp_login'),
    path('verify-otp/<str:email_or_phone>/', OTPVerifyView.as_view(), name='otp_verify'),
    path('resend-otp/<str:email_or_phone>/', ResendOTPView.as_view(), name='resend_otp'),
]
