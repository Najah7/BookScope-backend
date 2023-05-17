# ReadBookエンドポイント

## 目次
- [概要](#概要)
- [URL](#url)
    - [GET /readbook](#get-readbook)
    - [POST /readbook](#post-readbook)
    - [DELETE /readbook](#delete-readbook)


## 概要
読んだ本に関する情報を扱うエンドポイント

## URL

- ### GET /readbook

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |
| user_id    |      | string | ユーザID |

## Response

Status: 200 OK

```json
{
    {
        "book_id": "book_id",
        "title": "title",
        "isbn": "isbn",
        "author": "author",
        "publisher": "publisher",
        "price" : "price",
        "image": "image_url",
        "tags" : [
            {
            "tag_id": "tag_id",
            "tag": "tag"
            },
            {
            "tag_id": "tag_id",
            "tag": "tag"
            }
        ]
    },
    {
        "book_id": "book_id",
        "title": "title",
        "isbn": "isbn",
        "author": "author",
        "publisher": "publisher",
        "price" : "price",
        "image": "image_url",
        "tags" : [
        {
            "tag_id": "tag_id",
            "tag": "tag"
        },
        {
            "tag_id": "tag_id",
            "tag": "tag"
        }
    ]
    }, ...

    
}
```

- ### POST /readbook

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |
| isbn       | △    | string | ISBNコード |
| book_id    | △    | string | 本ID |

※△はどれか１つは必須

## Response

Status: 201 Created

```json
{
    "book_id": "book_id",
    "title": "title",
    "isbn": "isbn",
    "author": "author",
    "publisher": "publisher",
    "price" : "price",
    "image": "image_url",
    "tags" : [
        {
        "tag_id": "tag_id",
        "tag": "tag"
        },
        {
        "tag_id": "tag_id",
        "tag": "tag"
        }
    ]
}
```

- ### DELETE /readbook

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |
| read_book_id    | ○    | string | 本ID |

## Response

Status: 200 OK

```json
{
    "message": "success to delete a book you read"
}
```