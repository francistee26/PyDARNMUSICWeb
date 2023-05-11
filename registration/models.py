from django.db import models
from django.contrib.auth.models import AbstractUser
# from django import forms
# Create your models here.
class UserAccount(AbstractUser):
    USER_TYPE_ATMOSPHERIC_RESEARCH_STUDENT = "Atmospheric Research Student"
    USER_TYPE_ATMOSPHERIC_RESEARCH_SCIENTIST = "Atmospheric Research Scientist"
    USER_TYPE_US_CITIZEN = "US Citizen"
    USER_TYPES = [
        (USER_TYPE_ATMOSPHERIC_RESEARCH_STUDENT, "ATMOSPHERIC RESEARCH STUDENT"),
        (USER_TYPE_ATMOSPHERIC_RESEARCH_SCIENTIST, "ATMOSPHERIC RESEARCH SCIENTIST"),
        (USER_TYPE_US_CITIZEN, "US CITIZEN"),
    ]
    # username = forms.CharField(max_length=250,required=True)
    # email = forms.EmailField(required=True, unique=True)
    # password1 = 
    User_Type = models.CharField(max_length=250, choices=USER_TYPES)
    Request_For_SuperUser = models.BooleanField(default=False)

class RequestForSuperUserPrivileges(models.Model):
    username = models.CharField(max_length=250,blank=False)
    email = models.EmailField()
    Request_For_SuperUser = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(UserAccount, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)