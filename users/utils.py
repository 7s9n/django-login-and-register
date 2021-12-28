from django.conf import settings
from django.core.mail import send_mail

from django.utils.translation import gettext_lazy as _



def send_email(subject, message, to):
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to])

def send_activation_code(to, code):
    subject = _('Email Verification Code')
    message = _(f'Your verification code is {code}')
    send_email(subject, message, to)

def send_reset_password_code(to, code):
    subject = 'Password Reset Code'
    message = f'Your password reset code is {code}'
    send_email(subject, message, to)