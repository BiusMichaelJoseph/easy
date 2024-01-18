from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created

@receiver(reset_password_token_created)
def password_reset_token_created(sender,instance, reset_password_token, *args, **kwargs):
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key
        )
    }

    email_html_message = render_to_string('email/password_reset_email.html', context)
    emal_plaintext_message = render_to_string('email/password_reset_email.txt', context)

    msg = EmailMultiAlternatives(
        "Password Reset for {title}".format(title="My Hustle"),
        emal_plaintext_message,
        "noreply@yourdomain.com",
        [reset_password_token.user.email]
    )

    msg.attach_alternative(email_html_message, "text/html")
    msg.send()


