from django.urls import re_path
from .views import CreateUserAPIView

urlpatterns = [
    re_path(r'^create/$', CreateUserAPIView.as_view())
]