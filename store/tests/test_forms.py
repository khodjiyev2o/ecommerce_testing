from django.test import TestCase
from store.models import Product
from store.forms import ProductForm 


class TestForms(TestCase):
    
    def test_form_valid(self):
        form = ProductForm(data={
            'name':'product1',
            'price': 22.5
        })
        self.assertTrue(form.is_valid(),True)
        form.save()
        self.assertEquals(Product.objects.count(),1)


    def test_form_invalid(self):
        form = ProductForm(data={})
        self.assertFalse(form.is_valid(),False)
        self.assertEquals(Product.objects.count(),0)
        self.assertEquals(len(form.errors),2)