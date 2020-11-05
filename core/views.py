from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import UserRegistrationSerializer

class NewUserRegistration(viewsets.ViewSet):
    """
    New User Registration
    """
    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

