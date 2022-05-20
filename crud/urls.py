from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('blogpost', views.blogpostGetPostView.as_view()),
    path('blogpost/<int:pk>', views.blogpostView.as_view()),

]