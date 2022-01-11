from django.core.mail import send_mail
from django.conf import settings


def send_forget_password_mail(email, token):
    subject = "Your forget password link"
    message = f'Hi, Click on the link to reset password ----> http://127.0.0.1:8000/reset_pass/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    print("recipient_list : ", recipient_list)
    send_mail(subject, message, email_from, recipient_list)
    return True
