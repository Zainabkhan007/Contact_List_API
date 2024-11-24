from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class Register(GenericAPIView):
    serializer_class=RegisterSerializer
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Login(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        data = request.data
        username = data.get("username", "")
        password = data.get("password", "")
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

    