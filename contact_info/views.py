from django.shortcuts import render
from .models import *

from rest_framework.generics  import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class Contact_View(ListCreateAPIView):
    serializer_class=UserProfileSerializer
    permission_classes=[IsAuthenticated,]
    authentication_classes=[JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get_queryset(self):
        return UserProfile.objects.filter(owner=self.request.user)



class Contact_Detail(RetrieveUpdateDestroyAPIView):
    serializer_class=UserProfileSerializer
    permission_classes=[IsAuthenticated,]
    authentication_classes=[JWTAuthentication]
    lookup_field='id'
    
    def get_queryset(self):
        return UserProfile.objects.filter(owner=self.request.user)
