import pytest
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
 
pytestmark=pytest.mark.django_db
User=get_user_model()


def test_user_registeration(client):
    response=client.post(reverse('register'),{
        'first_name':'ahmed',
        'last_name':'khan',
        'username':'ahmedkhan',
        'password':'12345',
        'password_confirmation': '12345',
        'email':'ahmed@gmail.com'
      
                })
  
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username='ahmedkhan').exists()

    
    # Now attempt to log in
    response = client.post(reverse('login'), {
        'username': 'ahmedkhan',
        'password': '12345',
    })
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data





