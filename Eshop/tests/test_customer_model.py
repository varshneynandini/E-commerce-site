from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from store.models.customer import Customer

# class CustomerModelTest(TestCase):
#     def setUp(self):
#         # Create a sample customer
#         self.customer = Customer.objects.create(
#             first_name='John',
#             last_name='Doe',
#             phone='1234567890',
#             email='john@example.com',
#             password='password123'
#         )
#
#     def test_customer_creation(self):
#         """Test if customer is created properly"""
#         self.assertEqual(self.customer.first_name, 'John')
#         self.assertEqual(self.customer.last_name, 'Doe')
#         self.assertEqual(self.customer.phone, '1234567890')
#         self.assertEqual(self.customer.email, 'john@example.com')
#         self.assertEqual(self.customer.password, 'password123')

class CustomerModelTest(TestCase):
    def setUp(self):
        # Create a sample customer
        self.customer = Customer.objects.create(
            first_name='Neeru',
            last_name='Varshney',
            phone='1234567890',
            email='Varshney@example.com',
            password='password123'
        )

    def test_customer_creation(self):
        """Test if customer is created properly"""
        self.assertEqual(self.customer.first_name, 'Neeru')
        self.assertEqual(self.customer.last_name, 'Varshney')
        self.assertEqual(self.customer.phone, '1234567890')
        self.assertEqual(self.customer.email, 'Varshney@example.com')
        self.assertEqual(self.customer.password, 'password123')

    def test_register_method(self):
        """Test if the register method saves the customer"""
        new_customer = Customer(
            first_name='Aditi',
            last_name='Agrawal',
            phone='0987654321',
            email='Aditi@example.com',
            password='password456'
        )
        new_customer.register()
        self.assertTrue(Customer.objects.filter(email='Aditi@example.com').exists())

    def test_get_customer_by_email(self):
        """Test if get_customer_by_email method retrieves the correct customer"""
        retrieved_customer = Customer.get_customer_by_email('Varshney@example.com')
        self.assertEqual(retrieved_customer, self.customer)

    def test_isExists_method(self):
        """Test if isExists method correctly identifies existing customers"""
        self.assertTrue(self.customer.isExists())

    def test_isExists_method_nonexistent_customer(self):
        """Test if isExists method correctly identifies non-existent customers"""
        non_existent_customer = Customer(
            first_name='Non',
            last_name='Existent',
            phone='0000000000',
            email='nonexistent@example.com',
            password='password789'
        )
        self.assertFalse(non_existent_customer.isExists())