from django.test import TestCase, Client
from annonce.models import Categorie, Annonce, Comment, MpUser
from accounts.models import Profile
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
        # reverse urls 
        self.add_annonce_url = reverse('add_annonce' )
        self.annonce_detail_url = reverse('annonce_detail', args=['a302e83a-53c3-4daf-9810-f0acad98c222'])
        self.favorite_annonce_url = reverse('favorite_annonce', args=['a302e83a-53c3-4daf-9810-f0acad98c222'])
        self.favorite_list_url = reverse('favorite_list')
        self.message_url = reverse('message_list')
        self.annonce_list_url = reverse('annonce_list')
        self.annonce_delet_url = reverse('annonce_delete', args=['a302e83a-53c3-4daf-9810-f0acad98c222'])
        self.annonce_update_url = reverse('annonce_update', args=['a302e83a-53c3-4daf-9810-f0acad98c222'])
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
            'type_annonce': 'Jeux video',
            'price': 20.00,
            'categories': self.categorie,
            'description': 'super jeux',
            'owner':self.profile,
        })
        search_annonce = Annonce.objects.filter(title= 'Jeux avendre').first()
        self.assertEquals(search_annonce.price, 20.00)
        self.assertEquals(response.status_code, 302)
        
    def test_annonce_detail(self):
        self.client.login(username='wafisots', password='djamel2013')
        response = self.client.get('annonce/detail/a302e83a-53c3-4daf-9810-f0acad98c222')
        annonce_detail = get_object_or_404(Annonce, pk=self.annonce_create.id)
        comment = Comment.objects.filter(
            for_post=annonce_detail,
            reply=None
            ).order_by('-create_content')
        self.assertEquals(annonce_detail.product, 'Loisirs')

    