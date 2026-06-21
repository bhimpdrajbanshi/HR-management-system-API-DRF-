from django.urls import path
from . import views

from django.urls import path
from .views import *

urlpatterns = [
    path("api/csrf/", csrf_token_view),
    
    path("", LoginAPIView.as_view(), name="login"),
    path("api/logout/", LogoutAPIView.as_view()),
    path("api/profile/", ProfileAPIView.as_view()),
]