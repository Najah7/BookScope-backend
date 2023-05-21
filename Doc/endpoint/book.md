# Bookエンドポイント（読んだ本）

※読んだ本の編集のみ、公開。（読んだ本→登録されている本という流れでだけ、本のテーブルにデータが追加される）

## 目次
- [概要](#概要)
- [URL](#url)
    - [GET /book](#get-book)
    - [POST /book](#post-book)
    - [DELETE /book](#delete-book)


## 概要
読んだ本に関する情報を扱うエンドポイント

## URL

- ### GET /book

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| book_id    |      | string | 本ID |
| title      |      | string | タイトル |
| author     |      | string | 著者 |
| publisher  |      | string | 出版社 |
| isbn       |      | string | ISBNコード |
| key_word     |      | string | 検索ワード |

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
        "image_url": "image_url",
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
        "image_url": "image_url",
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

- ### POST /book

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| isbn       | △    | string | ISBNコード |
| title      | △    | string | タイトル |
| author     | △    | string | 著者 |
| publisher  | △    | string | 出版社 |
| image_url      | △    | string | 画像URL |
| tags       |      | array | タグ |

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
    "image_url": "image_url",
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

※△はどれか１つは必須

## Response

Status: 200 OK

```json
{
    "book_id": "book_id",
    "title": "title",
    "isbn": "isbn",
    "author": "author",
    "publisher": "publisher",
    "price" : "price",
    "image_url": "image_url",
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


- ### DELETE /book

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| read_book_id    | ○    | string | 本ID |

## Response

Status: 200 OK

```json
{
    "message": "success to delete a book you read"
}
```