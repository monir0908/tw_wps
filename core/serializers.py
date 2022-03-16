from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
        

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=[
            'first_name',
            'last_name',
            'mobile',
            'email'
        ]