from rest_framework import serializers
from .models import CustomRoles

class CustomRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomRoles
        fields = ['id', 'username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomRoles(
            username=validated_data['username'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
