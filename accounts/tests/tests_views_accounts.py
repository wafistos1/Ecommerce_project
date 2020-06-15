from django.test import TestCase, Client
from annonce.models import Categorie, Annonce, Comment, MpUser
from accounts.models import Profile
from annonce.forms import annonceFrom, categorieFrom, MpUserForm
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404 



class TestModels(TestCase):

    def setUp(self):
        self.client = Client()
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
        self.add_edit_url = reverse('edit')
        self.add_profile_url = reverse('profile' )
        self.add_list_annonces_url = reverse('list_annonces' )
        
        
     
    def test_home_template(self):
        self.client.force_login(self.profile)   
        response = self.client.get(self.add_edit_url)
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
    
    def test_edit_ok_get(self):
        self.client.force_login(self.profile)   
        response = self.client.get('/accounts/compte')
        print(response)
        self.assertEquals(response.status_code, 200)
    
    def test_list_annonces_ok_get(self):
        self.client.force_login(self.profile)   
        response = self.client.get('/accounts/list_annonces')
        print(response)
        self.assertEquals(response.status_code, 200)

    def test_list_annonces_down_get(self):
        self.client.force_login(self.profile)   
        response = self.client.get('/accounts/toto')
        print(response)
        self.assertEquals(response.status_code, 404)

    def test_form_edit_ok_get(self):
        self.client.force_login(self.profile) 
        response = self.client.post('/accounts/compte', data=self.data)
        print(response)
        self.assertEquals(response.status_code, 200)

   

