from django.urls import path, include

from accounts.views import UserAPIView
from .api import SimpleApI


urlpatterns = [
    path('api/hello', SimpleApI.as_view()),
    path('api/register', UserAPIView.as_view()),
    
]