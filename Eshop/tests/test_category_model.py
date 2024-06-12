from django.test import TestCase
from store.models.category import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create sample categories
        cls.category1 = Category.objects.create(name='Category 1')
        cls.category2 = Category.objects.create(name='Category 2')

    def test_category_creation(self):
        # Test if category is created properly
        self.assertEqual(self.category1.name, 'Category 1')
        self.assertEqual(self.category2.name, 'Category 2')

    def test_get_all_categories(self):
        # Test get_all_categories method
        categories = Category.get_all_categories()
        self.assertEqual(len(categories), 2)
        self.assertIn(self.category1, categories)
        self.assertIn(self.category2, categories)

    def test_str_representation(self):
        # Test __str__ method
        self.assertEqual(str(self.category1), 'Category 1')
        self.assertEqual(str(self.category2), 'Category 2')
