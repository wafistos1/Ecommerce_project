from django.db import models
import uuid

from django.urls import reverse
from accounts.models import Profile


# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=200)


class Annonce(models.Model):
    """
    class for Product user
    """
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    product = models.CharField(max_length=100,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description = models.TextField()
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    date = models.DateField( auto_now_add=True)
    image = models.ImageField(upload_to='image/', default='image_default.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('annonce_detail', args=[str(self.id)])