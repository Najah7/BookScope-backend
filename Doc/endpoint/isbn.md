# ISBNコード関係のエンドポイント

## 概要
下記のためのエンドポイント
- ISBNから本の情報を取得する
- ISBNのバーコードの画像をアップロードし、本の情報を取得する
- ISBNを使って、本の画像を取得する

## url

### GET /isbn

## パラメータ
| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| isbn       | ○    | string | ISBNコード |

### Response
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
```

### GET /isbn/image

## パラメータ
| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| isbn       | o    | string | ISBNコード |

### Response
```json
{
    "image_url": "https://example.com/image.jpg"
}
```

### POST /isbn/barcode

## パラメータ
| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| isbn       | ○    | string | ISBNコード |
| image      | ○    | file | 画像ファイル(バーコード) |


