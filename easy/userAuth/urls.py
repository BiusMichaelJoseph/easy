from django.urls import path, include
from .views import CustomSignupView, register_user, user_login, user_logout, change_password, reset_password_email
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm



urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('reset-password-email/', reset_password_email, name='reset-password-email'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password-reset-request/', reset_password_request_token, name='password-reset-request'),
    path('password-reset/confirm/', reset_password_confirm, name='password-reset-confirm'),
    path('accounts/register/', CustomSignupView.as_view(), name='account_signup'),
]