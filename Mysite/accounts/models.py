from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Adresse(models.Model):
    """ Class for adress user
    """
    rue = models.CharField(max_length=300)
    ville = models.CharField(max_length=300)
    Zip = models.CharField(max_length=300)
    pays = models.CharField(max_length=300)

    def __str__(self):
        return self.rue


class Profile(models.Model):
    """ Class for user registration
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='picture/', default='default.jpg')
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=100)

    def _str__(self):
        return self.user.username