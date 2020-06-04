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
        self.add_annonce_url = reverse('add_annonce' )
        self.annonce_detail_url = reverse('annonce_detail', args=[self.annonce_create.id])
        self.favorite_annonce_url = reverse('favorite_annonce', args=[self.annonce_create.id])
        self.favorite_list_url = reverse('favorite_list')
        self.message_url = reverse('message_list')
        self.message_mp_url = reverse('message', args=[self.profile.id])
        self.annonce_list_url = reverse('annonce_list')
        self.annonce_delet_url = reverse('annonce_delete', args=[self.annonce_create.id])
        self.annonce_update_url = reverse('annonce_update', args=[self.annonce_create.id])
        # client
        self.client = Client()
             
    def test_home_get(self):
            response = self.client.get('')
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed( 'base.html')
     
    def test_add_annonce_is_ok(self):
        # login a user
        self.client.login(username='wafisots', password='djamel2013')
        # 
        response = self.client.post(self.add_annonce_url, {
            'title': 'Jeux avendre',
            'product':' Loisirs',
            'type_annonce': 'Vente',
            'price': 20.00,
            'categories': self.categorie,
            'description': 'super jeux',
            'owner':self.profile,
        })
        search_annonce = Annonce.objects.filter(title= 'Jeux avendre').first()
        self.assertEquals(search_annonce.price, 20.00)
        self.assertEquals(response.status_code, 302)
       
    def test_annonce_detail(self):     
        response = self.client.get(self.annonce_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'annonce/detail.html')

    def test_annonce_list_GET(self):     
        response = self.client.get(self.annonce_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'annonce/home.html')
        
        
    def test_annonce_delete_GET(self):
        self.client.login(username='wafistos', password='djamel2013')   
        response = self.client.get(self.annonce_delet_url)
        self.assertEquals(response.status_code, 302)
        
        
    def test_annonce_update_GET(self):
        self.client.login(username='wafistos', password='djamel2013')   
        response = self.client.get(self.annonce_update_url)
        self.assertEquals(response.status_code, 302)
    
    
    def test_message_GET(self):
        self.client.login(username='wafistos', password='djamel2013')   
        response = self.client.get(self.message_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'annonce/message_list.html')
    
        
    def test_annonce_update_is_ok_GET(self):
        self.client.login(username='wafistos', password='djamel2013')   
        response = self.client.get(self.annonce_update_url)
        form = annonceFrom(self.data)
        self.assertTrue(form.is_valid())
        self.assertEquals(response.status_code, 302)
        
    def test_message_mp_GET(self):
        self.client.login(username='wafistos', password='djamel2013')   
        response = self.client.get(self.message_mp_url)
        mp_form = MpUserForm(self.data_message)
        f = mp_form.save(commit=False)
        f.sender = self.profile
        f.reciever = self.profile
        mp_form.save()
        self.assertTrue(mp_form.is_valid())
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'annonce/message.html')
        
    