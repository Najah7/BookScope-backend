# Bookエンドポイント

## 目次
- [概要](#概要)
- [URL](#url)
  - [GET /book](#get-book)
  - [POST /book](#post-book)
  - [PUT /book](#put-book)
  - [DELETE /book](#delete-book)

## 概要
本に関する情報を扱うエンドポイント

## URL

- ### GET /book

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |
| isbn       |     △ | string | ISBNコード |
| search     |      △| string | 検索ワード |
| title      |      △| string | タイトル |
| author     |      △| string | 著者 |
| publisher  |      △| string | 出版社 |
| tag        |      △| string | タグ |
| sort       |      △| string | ソート順 |

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

- ### POST /book

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |
| isbn       | ○    | string | ISBNコード |
| title      |      | string | タイトル |
| author     |      | string | 著者 |
| publisher  |      | string | 出版社 |
| tag        |      | string | タグ |
| image_url      |      | string（url） | 画像 |

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

- ### PUT /book

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |
| book_id    | △    | string | 本ID |
| isbn       |  △   | string | ISBNコード |
| title      |      | string | タイトル |
| author     |      | string | 著者 |
| publisher  |      | string | 出版社 |
| tag        |      | string | タグ |
| image_url      |      | string（url） | 画像 |

※どちらか１つは必須

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
| token      | ○    | string | トークン |
| book_id    | △    | string | 本ID |
| isbn       | △    | string | ISBNコード |

## Response

Status: 200 OK

```json
{
    "message": "success to delete book"
}
```