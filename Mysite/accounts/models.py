from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Profile(AbstractUser):
    """
    """
    picture = models.ImageField(default='default.jpg', upload_to='picture/')
    adress1 = models.CharField(max_length=255)
    adress2 = models.CharField(max_length=255, )
    ville = models.CharField(max_length=255)
    codezip = models.CharField(max_length=50)
    contry = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    discriptions = models.CharField(max_length=255)
    

    def __str__(self):
        return self.user.username