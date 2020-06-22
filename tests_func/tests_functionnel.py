from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from accounts.models import Profile
from annonce.models import Annonce, Image, Categorie
import time


class MySeleniumTests(LiveServerTestCase):
    def setUp(self):
        """
        """
        self.selenium = WebDriver(executable_path='C:/geckodriver.exe')
        self.selenium.implicitly_wait(10)
        self.profile = Profile.objects.create_user(
            username='wafistos6',
            first_name='wafi',
            last_name='mameri',
            email='wafi6@gmail.com',
            password='djamel2013',
            adress1='12 rue',
            adress2='Alger centre',
            ville='Alger centre',
            codezip='16000',
            contry='Algerie',
            phone='2131234',
            discriptions='Bonjour',
            picture='/media/picture/papy.jpeg',
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
            image='/media/picture/papy.jpeg',
        )

    def tearDown(self):
        self.selenium.quit()

    def test_login(self):
        """ Test login form
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        self.selenium.find_element_by_id("id_login").send_keys('wafistos6')
        self.selenium.find_element_by_id("id_password").send_keys('djamel2013')
        self.selenium.find_element_by_id('submitBtn').click()
        time.sleep(7)
        self.assertEquals(self.selenium.title, 'Yatach Home')

    def test_search(self):
        """ Test search form
        """

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        query = self.selenium.find_element_by_name("q")
        query.send_keys('console')
        self.selenium.find_element_by_id('searchBtn').click()
        self.assertEquals(self.selenium.title, 'Yatach Home')

    def test_add_annonce(self):
        url_add_annonce = "/annonce/add"
        profile = Profile.objects.all().first()
        print(profile.is_active)
        profile.is_active = True
        profile.save()
        print(profile.password)
        self.selenium.get('%s%s' % (self.live_server_url, url_add_annonce))
        self.selenium.find_element_by_id("id_login").send_keys('wafistos6')
        self.selenium.find_element_by_id("id_password").send_keys('djamel2013')
        self.selenium.find_element_by_id('submitBtn').click()
        self.selenium.find_element_by_id("id_title").send_keys('Jeux a vendre')
        self.selenium.find_element_by_id("id_product").send_keys('console')
        self.selenium.find_element_by_id("id_price").send_keys(200)
        self.selenium.find_element_by_id("id_type_annonce").send_keys('Vente')
        self.selenium.find_element_by_id("id_categories").send_keys('LOISIRS')
        self.selenium.find_element_by_id("id_description").send_keys('Jeux occasion')
        self.selenium.find_element_by_class_name('site-btn').click()

    # def test_add_user(self):
    #     url_add_annonce = "/accounts/signup/"
    #     self.selenium.get('%s%s' % (self.live_server_url, url_add_annonce))
    #     self.selenium.find_element_by_id("id_username").send_keys('wafi')
    #     self.selenium.find_element_by_id("id_first_name").send_keys('wafi')
    #     self.selenium.find_element_by_id("id_last_name").send_keys('MAMERI')
    #     self.selenium.find_element_by_id("id_email").send_keys('mameri.wafi@gmail.com')
    #     self.selenium.find_element_by_id("id_password1").send_keys('djamel2013')
    #     self.selenium.find_element_by_id("id_password2").send_keys('djamel2013')
    #     self.selenium.find_element_by_id("id_adress1").send_keys('134 rue des coucous')
    #     self.selenium.find_element_by_id("id_adress2").send_keys('Bis')
    #     self.selenium.find_element_by_id("id_phone").send_keys('1314421321')
    #     self.selenium.find_element_by_id("id_ville").send_keys('Alger')
    #     self.selenium.find_element_by_id("id_contry").send_keys('Algerie')
    #     self.selenium.find_element_by_id("id_codezip").send_keys('16000')
    #     self.selenium.find_element_by_id("id_discriptions").send_keys('DA Python')
    #     self.selenium.find_element_by_id("id_picture").send_keys('D:\DA_Python\Projet13\Mysite\picture\image_default.jpg')
    #     self.selenium.find_element_by_class_name('site-btn').click()
    #     self.assertEquals(self.selenium.title, '')