from django.test import TestCase
from annonce.models import Categorie, Annonce, Comment, MpUser
from accounts.models import Profile
from django.contrib.auth.models import User




class TestModels(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(name='Jeux')
        # self.user = User.objects.create_user('wafi', 'wafi@gmail.com', 'wafipass')
        self.profile=Profile.objects.create(
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