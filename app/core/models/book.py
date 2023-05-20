"""
Book Model
"""

from django.db import models as DjangoModels

from core import models as CoreModels


class BookModelManager(DjangoModels.Manager):
    """Book Model Manager"""

    # ===================== 一般的なクエリ =====================
    # NOTE:一応、_bookをつけることで、デフォルトのやつと区別している。名前を変更するかも

    def create_book_with_tags(self, title, isbn, price, image, book_tags):
        book = self.model(title=title, isbn=isbn, price=price, image=image)
        book.save()
        for tag in book_tags:
            book.tags.add(tag)
        return book

    def update_book_with_tags(self, book, title, isbn, price, image, book_tags):
        CoreModels.Book.objects.filter(id=book.id).update(
            title=title, isbn=isbn, price=price, image=image
        )
        book.tags.clear()
        for tag in book_tags:
            book.tags.add(tag)

    # ===================== 検索系 =====================

    def search_books_by_title(self, title):
        return self.filter(title__contains=title).all()

    def search_books_under_price(self, price):
        return self.filter(price__lte=price).all()

    def search_books_over_price(self, price):
        return self.filter(price__gte=price).all()

    def search_books_by_tag(self, tag):
        return self.filter(tags__name__contains=tag).all()

    # TODO: ソート系のマネージャを実装


class Book(DjangoModels.Model):
    class Meta:
        db_table = "books"
        app_label = "core"

    authors = DjangoModels.ManyToManyField(CoreModels.Author, related_name="books")
    publishers = DjangoModels.ManyToManyField(
        CoreModels.Publisher, related_name="books"
    )
    tags = DjangoModels.ManyToManyField(CoreModels.BookTag, related_name="books")

    title = DjangoModels.CharField(max_length=200)
    isbn = DjangoModels.CharField(max_length=200)
    image = DjangoModels.ImageField(upload_to="images/", null=True, blank=True)
    price = DjangoModels.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = DjangoModels.DateTimeField(auto_now_add=True)
    updated_at = DjangoModels.DateTimeField(auto_now=True)

    objects = BookModelManager()

    def __str__(self):
        return f"title: {self.title}  isbn: {self.isbn} image_path: {self.image}"
