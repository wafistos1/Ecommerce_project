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
        self.annonce_create = Annonce.objects.create(
            title='Jeux avendre',
            product='Loisirs',
            type_annonce='Jeux video',
            price=20.00,
            categories=self.categorie,
            description='super jeux',
            owner=self.profile,
            )
        
        
        
     
    def test_annonce_title_objects(self):
        self.assertEquals(self.annonce_create.title, 'Jeux avendre')
        
    def test_annonce_product_objects(self):
        self.assertEquals(self.annonce_create.product, 'Loisirs')
        
    def test_annonce_type_annonce(self):
        self.assertEquals(self.annonce_create.type_annonce, 'Jeux video')
        
    def test_annonce_price_product(self):
        self.assertEquals(self.annonce_create.price, 20.00)
        
    def test_annonce_categories_name(self):
        self.assertEquals(self.annonce_create.categories.name, 'Jeux')
        
    def test_annonce_owner_name_(self):
        self.assertEquals(self.annonce_create.owner.first_name, 'wafi')

    