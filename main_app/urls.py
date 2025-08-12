from django.urls import path

from main_app.views import verify
from main_app.apps import MainAppConfig

app_name = MainAppConfig.name

urlpatterns = [
    path("<uuid>/", verify, name="verify"),
]
