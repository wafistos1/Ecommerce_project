from django.test import TestCase
from annonce.models import Categorie, Annonce, Comment, MpUser
from accounts.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse




class TestModels(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(name='Jeux')
        # self.user = User.objects.create_user('wafi', 'wafi@gmail.com', 'wafipass')
        self.profile=Profile.objects.create(
            username='wafis',
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
        
     
    def test_profile_first_name(self):
        self.assertEquals(self.profile.first_name, 'wafi')
        
    def test_profile_last_name(self):
        self.assertEquals(self.profile.last_name, 'mameri')
    
    def test_profile_email(self):
        self.assertEquals(self.profile.email, 'wafi@gmail.com')
        
    def test_profile_password(self):
        self.assertEquals(self.profile.password, 'djamel2013')
        
    def test_profile_adress1(self):
        self.assertEquals(self.profile.adress1, '12 rue')
        
    def test_profile_adress2(self):
        self.assertEquals(self.profile.adress2, 'Alger centre')
    
    def test_profile_ville(self):
        self.assertEquals(self.profile.ville, 'Alger centre')
    
    def test_profile_codezip(self):
        self.assertEquals(self.profile.codezip, '16000')
        
    def test_profile_contry(self):
        self.assertEquals(self.profile.contry, 'Algerie')
    
    def test_profile_phone(self):
        self.assertEquals(self.profile.phone, '2131234')
    
    def test_profile_discriptions(self):
        self.assertEquals(self.profile.discriptions, 'Bonjour')
        
class SignupTests(TestCase): # new
   
    
    def setUp(self):
        self.response = self.client.get('/accounts/signup')
        self.username = 'nabil'
        self.first_name='nabil'
        self.last_name='mameri'
        self.email='nabil@gmail.com'
        self.password='djamel2013'
        self.picture='static/img/223.jpg'
        self.adress1='12 rue',
        self.adress2='Alger centre'
        self.ville='Alger centre'
        self.codezip='16000'
        self.contry='Algerie'
        self.phone='2131234'
        self.discriptions='Bonjour'
        
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 301)
        
    def test_signup_form(self):
        new_user = Profile.objects.create(
            username=self.username,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            password=self.password,
            picture=self.picture,
            adress1=self.adress1,
            adress2=self.adress2,
            ville=self.ville,
            codezip=self.codezip,
            contry=self.contry,
            phone=self.phone,
            discriptions=self.discriptions,
            )
        self.assertEqual(Profile.objects.all().count(), 1)
        self.assertEqual(Profile.objects.all()
        [0].username, self.username)
        self.assertEqual(Profile.objects.all()
        [0].email, self.email)