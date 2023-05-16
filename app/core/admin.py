from django.contrib import admin

from core import models

# Register your models here.

admin.site.register(models.CustomUser)
admin.site.register(models.FavoritePhrase)
admin.site.register(models.FavoritePhraseLike)
admin.site.register(models.Major)
admin.site.register(models.Rank)
admin.site.register(models.School)
admin.site.register(models.WroteHistory)
admin.site.register(models.ReadBook)
admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.BookTag)
admin.site.register(models.Publisher)
admin.site.register(models.Post)
admin.site.register(models.PostComment)
admin.site.register(models.PostLike)
