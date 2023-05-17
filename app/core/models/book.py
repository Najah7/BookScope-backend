from django.db import models as BaseModel

from core import models as CoreModels

class Book(BaseModel.Model):
    class Meta:
        db_table = "books"
        app_label = "core"

    title = BaseModel.CharField(max_length=200)
    isbn = BaseModel.CharField(max_length=200)
    image = BaseModel.ImageField(upload_to="images/", null=True, blank=True)
    price = BaseModel.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = BaseModel.DateTimeField(auto_now_add=True)
    updated_at = BaseModel.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"title: {self.title} author: {self.author} publisher: {self.publisher} isbn: {self.isbn} image: {self.image}"
