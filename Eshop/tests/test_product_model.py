from django.test import TestCase
from store.models.product import Product
from store.models.category import Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a sample category
        cls.category = Category.objects.create(name='Test Category')

        # Create a sample product
        cls.product = Product.objects.create(
            name='Test Product',
            price=100,
            category=cls.category,
            description='Test Description',
            # Create a simple uploaded file to use as an image
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_product_creation(self):
        """Test if product is created properly"""
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(self.product.image.name, 'uploads/products/test_image.jpg')

    def test_get_products_by_id(self):
        """Test get_products_by_id method"""
        products = Product.get_products_by_id([self.product.id])
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0], self.product)

    def test_get_all_products(self):
        """Test get_all_products method"""
        products = Product.get_all_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0], self.product)

    def test_get_all_products_by_categoryid(self):
        """Test get_all_products_by_categoryid method"""
        products = Product.get_all_products_by_categoryid(self.category.id)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0], self.product)
