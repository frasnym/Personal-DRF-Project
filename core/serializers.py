from rest_framework import serializers
from .models import UserRegistration


class UserRegistrationSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        """
        Custom error message
        """
        super(UserRegistrationSerializer, self).__init__(*args, **kwargs) # call the super() 
        for field in self.fields: # iterate over the serializer fields
            self.fields[field].error_messages['required'] = '%s field is required'%field # set the custom error message
            self.fields[field].error_messages['blank'] = '%s field cannot be blank'%field
    
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