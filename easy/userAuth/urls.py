

from django.urls import path
from .views import CustomUserCreateView

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='user-registration'),
]

