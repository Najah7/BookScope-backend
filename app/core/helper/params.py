def get_book_params_handler(request):
    book_id = request.GET.get("book_id")
    isbn = request.GET.get("isbn")
    title = request.GET.get("title")
    price = request.GET.get("price")
    image_url = request.GET.get("image_url")
    author = request.GET.get("author")
    publisher = request.GET.get("publisher")
    key_word = request.GET.get("key_word")
    tags = request.GET.get("tags")
    
    if tags:
        tags = tags.split(",")
    else:
        tags = ""
    
    return {
        "book_id": book_id,
        "isbn": isbn,
        "title": title,
        'price': price,
        "image_url": image_url,
        "author": author,
        "publisher": publisher,
        "key_word": key_word,
        "tags": tags,
    }

def post_book_params_handler(request):
    book_id = request.data.get("book_id")
    isbn = request.data.get("isbn")
    title = request.data.get("title")
    price = request.data.get("price")
    image_url = request.data.get("image_url")
    author = request.data.get("author")
    publisher = request.data.get("publisher")
    key_word = request.data.get("key_word")
    tags = request.data.get("tags")
    
    if tags:
        tags = tags.split(",")
    else:
        tags = ""
        
    
    return {
        "book_id": book_id,
        "isbn": isbn,
        "title": title,
        'price': price,
        "image_url": image_url,
        "author": author,
        "publisher": publisher,
        "key_word": key_word,
        "tags": tags,
    }