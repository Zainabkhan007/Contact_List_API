from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    phone_no=models.IntegerField()
    contact_pic=models.URLField(null=True)