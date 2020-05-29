from django.test import SimpleTestCase
from django.urls import reverse, resolve
from annonce.views import home, annonceListView, message_list, updateAnnonce, AnnonceDeletelView, add_annonce, annonceDetaiView, favorite, annonce_favorite_list, message_mp

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_resultats_url_resolves(self):
        url = reverse('add_annonce')
        self.assertEquals(resolve(url).func, add_annonce)

    def test_list_url_resolves(self):
        url = reverse('annonce_list')
        self.assertEquals(resolve(url).func.view_class, annonceListView)
        
    def test_detail_url_resolves(self):
        url = reverse('annonce_detail', args=['a302e83a-53c3-4daf-9810-f0acad98c222'])
        self.assertEquals(resolve(url).func, annonceDetaiView)
        
    def test_favorite_url_resolves(self):
        url = reverse('favorite_annonce', args=['a302e83a-53c3-4daf-9810-f0acad98c222'])
        self.assertEquals(resolve(url).func, favorite)
        
    def test_favorite_url_resolves(self):
        url = reverse('favorite_list')
        self.assertEquals(resolve(url).func, annonce_favorite_list)
        
    def test_message_url_resolves(self):
        url = reverse('message', args=[4])
        self.assertEquals(resolve(url).func, message_mp)
    
    def test_message_list_url_resolves(self):
        url = reverse('message_list')
        self.assertEquals(resolve(url).func, message_list)
        
    def test_delete_annonce_url_resolves(self):
        url = reverse('annonce_delete', args=['a302e83a-53c3-4daf-9810-f0acad98c222'])
        self.assertEquals(resolve(url).func.view_class, AnnonceDeletelView)
    
    def test_update_annonce_url_resolves(self):
        url = reverse('annonce_update', args=['a302e83a-53c3-4daf-9810-f0acad98c222'])
        self.assertEquals(resolve(url).func, updateAnnonce)