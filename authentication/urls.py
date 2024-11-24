from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)
urlpatterns = [

      path("register/",views.Register.as_view(),name='register'),
      path('login/', views.Login.as_view(),name='login'),

      path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]