"""
Test for book model
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models as CoreModels
from core.helper import test as test_helper

def create_book(params):
    """Create and return a new book."""
    title = params['title']
    isbn = params['isbn']
    price = params['price']
    image_url = params['image_url']
    book_tags = params['book_tags']
    book = CoreModels.Book.objects.create_book_with_tags(title, isbn, price, image_url, book_tags)
    return book

def update_book(book, params):
    """Update and return a book."""
    title = params['title']
    isbn = params['isbn']
    price = params['price']
    image_url = params['image_url']
    book_tags = params['book_tags']
    CoreModels.Book.objects.update_book_with_tags(book, title, isbn, price, image_url, book_tags)
    



class BookModelTests(TestCase):
    
    def setUp(self):
        self.sample_data = test_helper.sample_data_for_creating_book()
        self.sample_data_for_update = test_helper.sample_data_for_updating_book2()
    
    def test_create_book_with_success(self):
        """Test creating a new book with success"""
        
        book = create_book(self.sample_data)
            
        self.assertEqual(book.title, self.sample_data['title'])
        self.assertEqual(book.isbn, self.sample_data['isbn'])
        self.assertEqual(book.price, self.sample_data['price'])
        i = 0
        for tag in book.tags.all():
            self.assertIn(tag, self.sample_data['book_tags'])
    
    def test_update_book_with_success(self):
        """Test updating a book with success"""
        
        book = create_book(self.sample_data)
        update_book(book, self.sample_data_for_update)
        
        updated_book = CoreModels.Book.objects.get(id=book.id)
        
        self.assertEqual(updated_book.title, self.sample_data_for_update['title'])
        self.assertEqual(updated_book.isbn, self.sample_data_for_update['isbn'])
        self.assertEqual(updated_book.price, self.sample_data_for_update['price'])
        for tag in updated_book.tags.all():
            self.assertIn(tag, self.sample_data_for_update['book_tags'])
        
        