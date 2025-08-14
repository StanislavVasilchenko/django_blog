from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from django_blog import settings
from main_app.models import User
from main_app.tasks import send_verification_email


@receiver(post_save, sender=User)
def user_update(sender, instance, *args, **kwargs):

    if not instance.is_verified:
        send_verification_email.delay(instance.id)