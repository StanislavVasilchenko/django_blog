from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from django_blog import settings
from main_app.models import User


@receiver(post_save, sender=User)
def user_update(sender, instance, *args, **kwargs):

    if not instance.is_verified:
        send_mail(
            subject='Verify your account',
            message='Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse(
                'main_app:verify', kwargs={'uuid': str(instance.verification_uuid)}),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.email],
            fail_silently=False,
        )