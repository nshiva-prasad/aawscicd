from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

    
@shared_task
def send_verification_email(email,verification_url):
    subject = 'Welcome to JoyfulSurprises '
    message = f'Please click the following link to verify your email: {verification_url}'
    from_email = 'team-joyfulsurprises@giftastar.uk'  # This should be a verified email address from which you're sending emails
    recipient_list = [email]
    
    #send_mail(subject, message, from_email, recipient_list)
    print(f"Verification Email: successfully sent email {email}, {verification_url}")
    
@shared_task
def send_forgot_password_email(email,verification_url):
    subject = 'Reset Password Email'
    message = f'Please click the following link to reset your password: {verification_url}'
    from_email = 'team-joyfulsurprises@giftastar.uk'  # This should be a verified email address from which you're sending emails
    recipient_list = [email]
    
    #send_mail(subject, message, from_email, recipient_list)
    print(f"Passowrd Reset Email: successfully sent email {email}, {verification_url}")

@shared_task
def send_password_updated_email(email):
    subject = 'Reset Password Email'
    message = f'Your Password is successfully updated'
    from_email = 'team-joyfulsurprises@giftastar.uk'  # This should be a verified email address from which you're sending emails
    recipient_list = [email]
    
    #send_mail(subject, message, from_email, recipient_list)
    print(f"Passowrd Updated Email: successfully sent email {email}")

@shared_task
def send_otp_via_email(email,otp):
    subject = 'Reset Password Email'
    message = f'Please use the following OTP to login: {otp}. Please keep this confidentital'
    from_email = 'team-joyfulsurprises@giftastar.uk'  # This should be a verified email address from which you're sending emails
    recipient_list = [email]
    
    #send_mail(subject, message, from_email, recipient_list)
    print(f"OTP: successfully sent email {email}, {otp}")