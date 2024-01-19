
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create a user without saving to the database
        user = serializer.save()

        # Send email verification
        self.send_verification_email(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def send_verification_email(self, user):
        subject = 'Email Verification'
        message = f'Thank you for registering. Please click the link below to verify your email:\n\n{self.get_verification_link(user)}'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = user.email
        send_mail(subject, message, from_email, [to_email], fail_silently=False)

    def get_verification_link(self, user):
        # Customize this method to generate a unique verification link
        # For simplicity, a basic example is provided here
        return f'http://example.com/verify/{user.id}/{user.email_verification_token}/'


