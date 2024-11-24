from .models import *
# from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        exclude=["owner"]
        