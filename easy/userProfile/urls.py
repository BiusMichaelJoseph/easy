

from django.urls import path
from .views import UserProfileCreateView, UserProfileRetrieveUpdateView

urlpatterns = [
    path('create/', UserProfileCreateView.as_view(), name='create-user-profile'),
    path('', UserProfileRetrieveUpdateView.as_view(), name='retrieve-update-user-profile'),
]

