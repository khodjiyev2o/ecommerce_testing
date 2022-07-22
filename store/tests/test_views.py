from django.test import TestCase,Client
from django.urls import reverse
from store.models import Product


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.store_url = reverse('store')
        self.product_create_url = reverse('create_product')


    def test_store_view(self):
        response = self.client.get(self.store_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'store/store.html')


    def test_store_view_post(self):
        response = self.client.post(self.product_create_url,{
            'name' :'Image',
            'price' : '24.5'
        })
        self.assertEquals(response.status_code,302)
        self.assertEquals(Product.objects.count(),1)



    def test_create_product_noinput(self):
        response = self.client.post(self.product_create_url)
        self.assertEquals(response.status_code,200)
        self.assertEquals(Product.objects.count(),0)