from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template import Template, Context

from django_blog import settings
from django_blog.celery import app
from publish.models import Post

REPORT_TEMPLATE = """ 
                        Here's how you did till now: 
                        {% for post in posts %} 
                        "{{ post.title }}": viewed {{ post.view_count }} times | 
                        {% endfor %} 
                    """


@app.task
def send_view_count_report():
    for user in get_user_model().objects.filter(is_verified=True):
        posts = Post.objects.filter(author=user)
        if not posts:
            continue
        template = Template(REPORT_TEMPLATE)
        send_mail(
            subject='Your Django_celery Project Activity',
            message=template.render(Context({'posts': posts})),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
