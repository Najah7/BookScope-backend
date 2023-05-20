# Postエンドポイント

### 目次


## 概要
投稿に関する情報を扱うエンドポイント

## URL

- ### GET /post

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      |   o   | string | トークン |
| search     |   △   | string | 検索ワード |
| book_name  |   △   | string | 本ID |
| writer     |   △   | string | 投稿者 |
| tags        |   △   | array | タグ |
| sort       |   △   | string | ソート順 |

## Response

Status: 200 OK

```json
{
  "post_id": "post_id",
  "book_id": "book_id",
  "user_id": "user_id",
  "title": "title",
  "content": "content",
  "created_at": "created_at",
  "updated_at": "updated_at",
}
```

- ### POST /post

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| post_id    |      | string | 投稿ID |
| title      | ○    | string | タイトル |
| content    | ○    | string | 内容 |
| tags       |      | array | タグ |

## Response

```json
{
  "post_id": "post_id",
  "book_id": "book_id",
  "user_id": "user_id",
  "title": "title",
  "content": "content",
  "created_at": "created_at",
  "updated_at": "updated_at",
}
```

- ### PUT /post

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| post_id    | ○    | string | 投稿ID |
| book_id    |      | string | 本ID |3
| title      |      | string | タイトル |
| content    |      | string | 内容 |

## Response

```json
{
  "post_id": "post_id",
  "book_id": "book_id",
  "user_id": "user_id",
  "title": "title",
  "content": "content",
  "created_at": "created_at",
  "updated_at": "updated_at",
}
```

- ### DELETE /post

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| post_id    | ○    | string | 投稿ID |

## Response

```json
{
  "message" : "success to delete post"
}
```

