from django.test import TestCase,Client
from django.urls import reverse
from store.models import Product


class TestViews(TestCase):
    def setUp(self):
        Product.objects.create(name='product1',price='22.5')
        self.client = Client()
        self.store_url = reverse('store')
        self.product_create_url = reverse('create_product')
        self.product_detail_url = reverse('product_detail',args=["1"])

    def test_store_view(self):
        response = self.client.get(self.store_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'store/store.html')



    def test_product_detail_view(self):
        response = self.client.get(self.product_detail_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'store/product_detail.html')



    def test_store_view_post(self):
        response = self.client.post(self.product_create_url,{
            'name' :'Image',
            'price' : '24.5'
        })
        self.assertEquals(response.status_code,302)
        self.assertEquals(Product.objects.count(),2)



    def test_create_product_noinput(self):
        response = self.client.post(self.product_create_url)
        self.assertEquals(response.status_code,200)
        self.assertEquals(Product.objects.count(),1)


    