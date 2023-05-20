from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models as CoreModels
from core.helper import test as test_helper

class PostModelTest(TestCase):
    """Test for post model"""
    
    def setUp(self, methodName: str = "runTest") -> None:
        super().setUp()
        self.user = test_helper.create_tuser()
        self.book = test_helper.create_sample_book()
        self.tags = test_helper.create_sample_post_tags(num_tag=3)
        self.read_book = test_helper.create_read_book(self.user, self.book)
        self.sample_data = test_helper.sample_data_for_creating_post()
        self.sample_data_for_update = test_helper.sample_data_for_updating_post()
    
    def tearDown(self) -> None:
        super().tearDown()
        if self.read_book is not None:
            self.read_book.delete()
        self.user.delete()
        self.book.delete()
        
    
        
    def test_create_post_with_tags_with_success(self):
        """Test creating a new post with relation with success"""
        
        post = CoreModels.Post.objects.create_post_with_tags(
            user=self.user,
            read_book=self.read_book,
            title=self.sample_data['title'],
            content=self.sample_data['content'],
            tags=self.tags
        )
        
        
        
        # 値の確認
        self.assertEqual(post.title, self.sample_data['title'])
        self.assertEqual(post.content, self.sample_data['content'])
        
        
        # リレーションの確認
        user = get_user_model().objects.get(id=self.user.id)
        self.assertEqual(user, self.user)
        book = CoreModels.Book.objects.get(id=self.book.id)
        self.assertEqual(book, self.book)
        
    def test_update_post_with_tags_with_success(self):
        
        post = CoreModels.Post.objects.create_post_with_tags(
            user=self.user,
            read_book=self.read_book,
            title=self.sample_data['title'],
            content=self.sample_data['content'],
            tags=self.tags
        )
        
        CoreModels.Post.objects.update_post_with_tags(
            post=post,
            title=self.sample_data_for_update['title'],
            content=self.sample_data_for_update['content'],
            tags=self.sample_data_for_update['tags']   
        )
        
        # 値の確認
        post = CoreModels.Post.objects.get(id=post.id)
        self.assertEqual(post.title, self.sample_data_for_update['title'])
        self.assertEqual(post.content, self.sample_data_for_update['content'])
        
        # リレーションの確認
        user = get_user_model().objects.get(id=self.user.id)
        self.assertEqual(user, self.user)
        book = CoreModels.Book.objects.get(id=self.book.id)
        self.assertEqual(book, self.book)
        