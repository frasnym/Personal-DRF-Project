from rest_framework import serializers
from .models import UserRegistration


class UserRegistrationSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Check if username is contain space
        """
        if " " in data["username"]:
            raise serializers.ValidationError(
                {"username": "value must not contain space"}
            )
        return data

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