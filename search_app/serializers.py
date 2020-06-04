from rest_framework import serializers
from annonce.models import Annonce, Categorie

class AnnonceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Annonce
        list_fields = ('type_annonce',  'categories',  'price', 'created')      
