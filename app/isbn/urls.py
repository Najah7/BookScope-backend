from django.urls import path

from . import views

urlpatterns = [
    path("search", views.BookInfoView.as_view()),
    path("image", views.BookImageView.as_view()),
    path("barcode", views.BarcodeView.as_view()),
]

