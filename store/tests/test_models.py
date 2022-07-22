from django.test import TestCase,Client
from django.urls import reverse
from store.models import Product,Order,OrderItem,Customer,User



class TestModels(TestCase):
    def setUp(self):
        product = Product.objects.create(name='product1',price='22.5')
        user = User.objects.create(username="Samandar")
        customer = Customer.objects.get(user=user)
        order = Order.objects.create(customer=customer)
        orderitem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=2,
            )
    def test_customer_create(self):
        self.assertEquals(Customer.objects.count(),1)

    def test_order(self):
        self.assertEquals(Order.objects.count(),1)
        self.assertEquals(Order.objects.first().get_cart_total,45.00)
    def test_order_item(self):
        self.assertEquals(OrderItem.objects.count(),1)
        self.assertEquals(OrderItem.objects.get(id=1).get_total,45.00)