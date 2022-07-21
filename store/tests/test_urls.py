


from django.test import SimpleTestCase
from django.urls import reverse,resolve
from store.views import store,cart,checkout,updateItem,ProductCreateView

class TestUrls(SimpleTestCase):

    def test_store_urls(self):
        url = reverse('store')
        self.assertEquals(resolve(url).func,store)
        
    def test_cart_urls(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func,cart)

    def test_checkout_urls(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func,checkout)

    def test_update_item_urls(self):
        url = reverse('update_item')
        self.assertEquals(resolve(url).func,updateItem)
    def test_create_product_urls(self):
        url = reverse('create_product')
        self.assertEquals(resolve(url).func.view_class,ProductCreateView)