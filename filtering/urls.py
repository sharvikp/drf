from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('ok', views.IntroductionViewSet, basename='course')

urlpatterns = [
    path('filtering/', views.IntroductionViewSet.as_view({'get': 'list'}))
    # path('filtering', include(router.urls))
]

