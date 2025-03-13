from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.CharField(max_length=50,null=True,blank=True)
    mobile_no = models.PositiveIntegerField(null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.user.username
