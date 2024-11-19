# src/backend/api/auth.py

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow any user to access this endpoint
def register(request):
    """
    User registration endpoint.
    """
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

    user = User(username=username, email=email, password=make_password(password))
    user.save()

    return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow any user to access this endpoint
def login(request):
    """
    User login endpoint.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)