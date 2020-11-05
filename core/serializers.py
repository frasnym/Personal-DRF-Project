from rest_framework import serializers
from .models import UserRegistration


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = [
            "username",
            "password",
            "full_name",
            "email_address",
            "phone_number",
            "current_address",
        ]