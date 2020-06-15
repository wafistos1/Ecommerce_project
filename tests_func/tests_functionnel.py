from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.urls import reverse
from accounts.models import Profile
from annonce.models import Annonce, Image, Comment, Categorie, MpUser
from selenium.webdriver.common.keys import Keys
import time 
import requests
from selenium import webdriver

class MySeleniumTests(LiveServerTestCase):
    def setUp(self):
        self.selenium = WebDriver(executable_path='C:/geckodriver.exe')
        self.selenium.implicitly_wait(10)
        self.profile = Profile.objects.create(
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
        self.categorie = Categorie.objects.create(name='Vente')
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
    def tearDown(self):
        self.selenium.quit()

       
    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        self.selenium.find_element_by_id("id_login").send_keys('wafistos6')
        self.selenium.find_element_by_id("id_password").send_keys('djamel2013')
        self.selenium.find_element_by_id('submitBtn').click()
        self.assertEquals(self.selenium.title, 'Connexion')


    def test_search(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        query = self.selenium.find_element_by_name("q")
        query.send_keys('console')
        self.selenium.find_element_by_id('searchBtn').click()
        self.assertEquals(self.selenium.title, 'Yatach Home')

        

    # def test_rating(self):
    #     url_rating = f"/detail_favori/{self.favorite.id}"
    #     self.selenium.get('%s%s' % (self.live_server_url, url_rating))
    #     self.selenium.find_element_by_id("id_username").send_keys('wafistos4')
    #     self.selenium.find_element_by_id("id_password").send_keys('djamel2013')
    #     self.selenium.find_element_by_id('submitBtn').click()
    #     self.selenium.find_element_by_xpath('//div[@class="rating"]/a[@id="rate_id"]').click()