from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'phone', 'full_name')

class LoginForm(forms.Form):
    email_or_phone = forms.CharField(label="Email or Phone", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    
class ForgotPasswordForm(forms.Form):
    email_or_phone = forms.CharField(label="Email or Phone", max_length=100)
    
class ResetPasswordForm(forms.Form):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return cleaned_data

class OTPLoginForm(forms.Form):
    email_or_phone = forms.CharField(label="Email or Phone", max_length=100)
    
class OTPVerifyForm(forms.Form):
    otp_code = forms.CharField(label="Enter OTP", required=True, max_length=6)
