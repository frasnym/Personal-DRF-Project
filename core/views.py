from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .serializers import UserRegistrationSerializer


class NewUserRegistration(viewsets.ViewSet):
    """
    New User Registration
    """
    # ? Class Scope Renderer: Use for generate custom Response message
    renderer_classes = [JSONRenderer] 

    def create(self, request):
        # ? Declare Response Message
        respMessage = {
            "success": False,
            "message": None,
        }
        # ? Set Serializer
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # TODO check username does not contain space
            # TODO multi language response
            # TODO one way encrypt password 
            # serializer.save()
            respMessage["success"] = True
            respMessage["message"] = 'Process Success'
            respMessage["data"] = {
                'username': serializer.data['username'],
                'email_address': serializer.data['email_address'],
                'phone_number': serializer.data['phone_number'],
            }
            return Response(respMessage, status=status.HTTP_201_CREATED)

        respMessage["message"] = f'{list(serializer.errors.values())[0][0]}: {list(serializer.errors.keys())[0]}'
        return Response(respMessage, status=status.HTTP_400_BAD_REQUEST)
