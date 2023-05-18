# アップロードエンドポイント

## 概要
画像をアップロードするエンドポイントです。

##　url

### POST /upload/user_icon

## パラメータ
| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |
| image      | ○    | file | 画像ファイル |

## Response

```json
{
    "status": "success",
    "message": "Success to upload image",
    "data": {
        "image_url": "https://s3-ap-northeast-1.amazonaws.com/.../icon/.../icon.png"
    }
}
```

### POST /upload/book_cover

## パラメータ
| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |
| image      | ○    | file | 画像ファイル |

## Response

```json
{
    "status": "success",
    "message": "Success to upload image",
    "data": {
        "image_url": "https://s3-ap-northeast-1.amazonaws.com/.../book_cover/.../book_cover.png"
    }
}
```
