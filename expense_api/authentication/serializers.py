from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        max_length=68,
        min_length=6,
        write_only=True)

    class Meta:
        model=User
        fields=['email','username','password']

    def validate(self,attrs):
        username=attrs.get('username','')
        email=attrs.get('email','')

        if not username.isalnum():
            raise serializers.ValidationError(
                'The userame should only be alphanumeric characters.'
            )
        return attrs
        
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class EmailVerficatioSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=555)
    class Meta:
        model=User
        fields=['token']