from rest_framework import serializers
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
        read_only_fields=(
            'alias',
        )
        