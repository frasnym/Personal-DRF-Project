from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    NewUserRegistration
)

router = DefaultRouter()
router.register(r'register', NewUserRegistration, basename='new-user-registration')

urlpatterns = [
    # ViewSet
    path('user/', include(router.urls)),
]
