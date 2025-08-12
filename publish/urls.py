from django.urls import path
from publish.apps import PublishConfig
from publish.views import view_post

app_name = PublishConfig.name

urlpatterns = [
    path('<slug:slug>/', view_post, name='view_post')
]