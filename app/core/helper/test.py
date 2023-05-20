import decimal
import random
import string
import datetime

from django.contrib.auth import get_user_model
from core import models as CoreModels
from django.utils import timezone




def create_tuser(email='testuser@example.com', password='testpass123'):
    """Create anf retun a new user."""
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '@example.com'
    return get_user_model().objects.create_user(email, password)

def create_sample_book_tags(num_tag, prefix='test tag'):
    """Create and return a new tags for book."""
    tags = []
    for i in range(0, num_tag):
        tag_name = prefix + ' ' + str(i)
        tag, created = CoreModels.BookTag.objects.get_or_create(name=tag_name)
        if created:
            tag.save()
        tags.append(tag)
    return tags

def create_sample_post_tags(num_tag, prefix='test tag'):
    """Create and return a new tags for post."""
    tags = []
    for i in range(0, num_tag):
        tag_name = prefix + ' ' + str(i)
        tag, created = CoreModels.PostTag.objects.get_or_create(name=tag_name)
        tags.append(tag)
    return tags


def create_sample_book(title='test title', isbn='978-4-00-310101-1', price=1000, image_url='https://example.com/test.jpg', tags=create_sample_book_tags(2)):
    """Create and return a new book."""
    book = CoreModels.Book.objects.create_book_with_tags(title, isbn, price, image_url, tags)
    return book

def create_read_book(user, book):
    """Create and return a new read book."""
    read_book = CoreModels.ReadBook.objects.model(
        read_at=timezone.now(),
        user=user,
        book=book
    )
    read_book.save()
    return read_book

def sample_data_for_creating_book():
    return {
        'title': 'test title',
        'isbn': '978-4-00-310101-1',
        'price': decimal.Decimal('1000.00'),
        'image_url': 'https://example.com/test.jpg',
        'book_tags': create_sample_book_tags(2),
    }
    
def sample_data_for_updating_book2():
    return {
        'title': 'test title2',
        'isbn': '978-4-00-310101-2',
        'price': decimal.Decimal('2000.00'),
        'image_url': 'https://example.com/test2.jpg',
        'book_tags': create_sample_book_tags(2, 'test tag'),
    }
    
def sample_data_for_creating_post():
    return {
        'title': 'test title',
        'content': 'test content',
        'tags': create_sample_post_tags(2),
    }
    
def sample_data_for_updating_post():
    return {
        'title': 'test title2',
        'content': 'test content2',
        'tags': create_sample_post_tags(2, 'test tag'),
    }

def sample_data_for_creating_read_book():
    return {
        'read_at': datetime.datetime.now(),
        'user': create_tuser(),
        'book': create_sample_book(),
    }

def sample_data_for_updating_read_book():
    return {
        'read_at': datetime.datetime.now(),
        'user': create_tuser(),
        'book': create_sample_book(),
    }
