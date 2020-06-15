
from django.test import TestCase, Client
from annonce.models import Categorie, Annonce, Comment, Image
from accounts.models import Profile
from annonce.forms import annonceFrom, MpUserForm, ImageForm
from django.urls import reverse
from django.forms import modelformset_factory


class TestModels(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(name='EMPLOI')
        # self.user = User.objects.create_user('wafi', 'wafi@gmail.com', 'wafipass')
        self.profile=Profile.objects.create(
            username='wafistos6',
            first_name='wafi',
            last_name='mameri',
            email='wafi6@gmail.com',
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
        self.images_annonce = Image.objects.create(
            annonce_images=self.annonce_create,
            image='static/img/123.jpg',
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
        self.assertTemplateUsed('base.html')

    def test_favorite_get(self):
        self.client.force_login(self.profile)
        response = self.client.get(self.favorite_list_url)
        self.assertEquals(response.status_code, 200)
    
    def test_update_get(self):
        self.client.force_login(self.profile)
        response = self.client.get(self.annonce_update_url)
        self.assertEquals(response.status_code, 200)

    def test_add_annonce_is_ok(self):
        # login a user
        self.client.force_login(self.profile)  
        response = self.client.post(self.add_annonce_url, {
            'title': 'Jeux avendre',
            'product': 'Loisirs',
            'type_annonce': 'Vente',
            'price': 20.00,
            'categories': self.categorie,
            'description': 'super jeux',
            'owner': self.profile,
        })
        search_annonce = Annonce.objects.filter(title= 'Jeux avendre').first()
        self.assertEquals(search_annonce.price, 20.00)
        self.assertEquals(response.status_code, 200)

    def test_annonce_detail(self):     
        response = self.client.get(self.annonce_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'annonce/detail.html')

    def test_annonce_list_GET(self):     
        response = self.client.get(self.annonce_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'annonce/home.html')

    def test_annonce_delete_GET(self):
        self.client.force_login(self.profile)  
        response = self.client.get(self.annonce_delet_url)
        self.assertEquals(response.status_code, 200)

    def test_message_GET(self):
        self.client.force_login(self.profile)  
        response = self.client.get(self.message_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'annonce/message_list.html')

    def test_message_mp_GET(self):
        self.client.force_login(self.profile)    
        response = self.client.get(self.message_mp_url)
        mp_form = MpUserForm(self.data_message)
        f = mp_form.save(commit=False)
        f.sender = self.profile
        f.reciever = self.profile
        mp_form.save()
        self.assertTrue(mp_form.is_valid())
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'annonce/message.html')

    def test_updateAnnonce_is_Ok(self):
        data = {
            'title': 'Jeux avendre',
            'product':' Loisirs',
            'type_annonce': 'Vente',
            'price': 20.00,
            'categories': self.categorie,
            'description': 'super jeux',
            'owner': self.profile,
            'image': self.images_annonce, 
        }
        self.client.force_login(self.profile)  
        response = self.client.get('/annonce/add')
        annonce = Annonce.objects.filter(title='Jeux avendre').first()
        self.assertEquals(annonce.title, 'Jeux avendre')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('add.html')
        form = annonceFrom(data=data)
        # ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=4, max_num=4, validate_max=True) 
        # form_image = ImageFormSet(self.images_annonce)
        # print(ImageFormSet.errors)    
        self.assertTrue(form.is_valid())
        # self.assertTrue(ImageFormSet.is_valid())

    def test_formset(self):
        ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=4, max_num=4, validate_max=True) 
        formset = ImageFormSet()
        self.assertEqual(formset.max_num, 4)
        self.assertTrue(formset.validate_max)

    def test_form_is_ok(self):
        count = Annonce.objects.all().count()
        print(f'test form count1 {count}')
        self.client.force_login(self.profile)  
        response = self.client.post(reverse('add_annonce'), data={
            'title': 'Voiture a vendre',
            'product': 'Loisirs',
            'type_annonce': 'Vente',
            'price': 20.00,
            'categories': self.categorie,
            'description': 'super jeux',
            'owner': self.profile,
            'image': self.images_annonce, 
        })
        # print(response)
        # user = Profile.objects.all().first()
        # print(user.password)
        # print(Profile.objects.all())
        count1 = Annonce.objects.all().count()
        print(f'test form count2 {count1}')
        search = Annonce.objects.create(title= 'Voiture',
                                        product='Loisirs',
                                        price=20.00,
                                        categories=self.categorie,
                                        description='super jeux',
                                        owner=self.profile,
                                        )
        self.assertEquals(search.title, 'Voiture')
        self.assertEquals(response.status_code, 200)
        
    # def test_form_is_not_ok(self):
    #     self.client.login(username=self.profile.username, password=self.profile.password)
    #     response = self.client.post('/annonce/add', {})
    #     search = Annonce.objects.get(title='Voiture a vendre')
    #     self.assertEquals(search.title, 'Voiture a vendr')
    #     self.assertEqual(response.status_code, 302)

    def test_profile(self):
        count = Profile.objects.all().count()
        profile = Profile.objects.create(
            username='wafistos7',
            first_name='wafi',
            last_name='mameri',
            email='wafi7@gmail.com',
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
        profile.save()
        count2 = Profile.objects.all().count()
        print(f'{count},  {count2}' )
        self.assertEqual(profile.username, 'wafistos7')
        self.assertEqual(count2, count +1)
        
    def test_favorite_filter(self):
        self.client.force_login(self.profile)  
        favorite_object = Annonce.objects.get(owner=self.profile.id)
        favorite_object.save()

        favorite_object.favorite.add(self.profile)
        