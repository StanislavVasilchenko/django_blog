from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse

from django_blog import settings
from django_blog.celery import app


@app.task
def send_verification_email(user_id):
    user_model = get_user_model()
    try:
        user = user_model.objects.get(pk=user_id)
        send_mail(
            'Verify your  account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse(
                'main_app:verify', kwargs={'uuid': str(user.verification_uuid)}
            ),
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    except user_model.DoesNotExist:
        print(f"Tried to send verification email to non-existing user {user_id}")
