from django.db import models


class Book(models.Model):
    class Meta:
        db_table = "books"
        app_label = "core"

    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"title: {self.title} author: {self.author} publisher: {self.publisher} isbn: {self.isbn} image: {self.image}"
