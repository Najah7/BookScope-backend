import os
import requests

def fetch_book_data_by_isbn(isbn):
    url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
    params = {
        "format": "json",
        "isbn": isbn,
        "applicationId": os.environ.get("RAKUTEN_APP_ID"),
    }
    res = requests.get(url, params=params).json()
    
    book_info = res.get('Items')[0]['Item']
    return {
        "title": book_info.get("title"),
        "isbn": book_info.get("isbn"),
        "author": book_info.get("author"),
        "publisher": book_info.get("publisherName"),
        "price": book_info.get("itemPrice"),
        "image_url": book_info.get("largeImageUrl")
    }

def fetch_book_data_by_title(title):
    url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
    params = {
        "format": "json",
        "title": title,
        "applicationId": os.environ.get("RAKUTEN_APP_ID"),
    }
    res = requests.get(url, params=params)
    books = res.json()['Items']
    book_info = {}
    for book in books:
        new_book_info = {
            "title": book["title"],
            "author": book["author"],
            "publisher": book["publisherName"],
            "price": book["itemPrice"],
            "image_url": book["largeImageUrl"]
        }
        book_info.append(new_book_info)
    return book_info
    

def fetch_book_data_by_author(author):
    url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
    params = {
        "format": "json",
        "author": author,
        "applicationId": os.environ.get("RAKUTEN_APP_ID"),
    }
    res = requests.get(url, params=params)
    books = res.json()['Items']
    book_info = {}
    for book in books:
        new_book_info = {
            "title": book["title"],
            "author": book["author"],
            "publisher": book["publisherName"],
            "price": book["itemPrice"],
            "image_url": book["largeImageUrl"]
        }
        book_info.append(new_book_info)
    return book_info

def fetch_book_data_by_publisher(publisher):
    url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
    params = {
        "format": "json",
        "publisherName": publisher,
        "applicationId": os.environ.get("RAKUTEN_APP_ID"),
    }
    res = requests.get(url, params=params)
    books = res.json()['Items']
    book_info = {}
    for book in books:
        new_book_info = {
            "title": book["title"],
            "author": book["author"],
            "publisher": book["publisherName"],
            "price": book["itemPrice"],
            "image_url": book["largeImageUrl"]
        }
        book_info.append(new_book_info)
    return book_info