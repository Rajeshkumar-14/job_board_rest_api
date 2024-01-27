from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer 

@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save() 
        user.set_password(request.data["password"])
        user.save()
        return Response("User created successfully", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):
    try:
        user = get_object_or_404(User, username=request.data["username"])
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

    if not user.check_password(request.data["password"]):
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})
