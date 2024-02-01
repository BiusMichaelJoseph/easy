from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import update_session_auth_hash
from .serializers import ChangePasswordSerializer, ResetPasswordEmailSerializer
from allauth.account.views import SignupView
from allauth.account.utils import send_email_confirmation

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Fixed: Added parentheses to call the save method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)

        # Send email confirmation
        send_email_confirmation(self.request, self.user)

        return response


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            # Attempt to get the user by email
            user = CustomUser.objects.get(email=username)
        except ObjectDoesNotExist:
            # If the user is not found by email, try authenticating with username/password
            user = authenticate(username=username, password=password)

        if user:
            # If the user is found, generate or get the token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # If neither email nor username/password authentication succeeds, return an error
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            #Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['POST'])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            # Your password change logic here using the serializer.validated_data
            return Response({'message': 'Password successfully changed.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reset_password_email(request):
    if request.method == 'POST':
        serializer = ResetPasswordEmailSerializer(data=request.data)
        if serializer.is_valid():
            # Your logic for initiating a password reset via email
            return Response({'message': 'Password reset email sent.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

