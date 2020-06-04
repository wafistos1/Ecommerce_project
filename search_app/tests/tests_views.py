from django.test import TestCase, Client
from annonce.models import Categorie, Annonce, Comment, MpUser
from accounts.models import Profile
from annonce.forms import annonceFrom, categorieFrom, MpUserForm
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404 



class TestModels(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(name='Jeux')
        # self.user = User.objects.create_user('wafi', 'wafi@gmail.com', 'wafipass')
        self.profile=Profile.objects.create(
            username='wafistos',
            first_name='wafi',
            last_name='mameri',
            email='wafi@gmail.com',
            password='djamel2013',
            picture='static/img/23.jpg',
            adress1='12 rue',
            adress2='Alger centre',
            ville='Alger centre',
            codezip='16000',
            contry='Algerie',
            phone='2131234',
            discriptions='Bonjour',  
        )
        self.annonce_create = Annonce.objects.create(
            title='Jeux avendre',
            product='Loisirs',
            type_annonce='Jeux video',
            price=20.00,
            categories=self.categorie,
            description='super jeux',
            owner=self.profile,
            )
        self.comment = Comment.objects.create(
            commented_by=self.profile,
            for_post=self.annonce_create,
            content='Je suis un commentaires',
        )
        self.data = {
            'title': 'Jeux avendre',
            'product':' Loisirs',
            'type_annonce': 'Vente',
            'price': 20.00,
            'categories': self.categorie,
            'description': 'super jeux',
            'owner':self.profile,  
        }
        self.data_message = { 
            'subject': 'test',
            'message': 'Hi',  
        }
        # reverse urls 
        self.add_search_url = reverse('search' )
        self.add_filter_url = reverse('filter' )
        
        self.client = Client()
        
     
    def test_search_ok_get(self):
            response = self.client.get(self.add_search_url)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed( 'search_app/search.html')
    
    
    def test_filter_ok_get(self):
        response = self.client.post(
            reverse('filter'),
            data={'categoriese': 'VÉHICULES '},
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )     
        self.assertEqual(200, response.status_code)
        self.assertEquals(response.status_code, 200)