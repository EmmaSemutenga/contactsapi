from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'contacts', views.ContactViewSet)


urlpatterns = [
    path('', include(router.urls)),
]