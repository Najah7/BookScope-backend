# Tokenエンドポイント

## token

### 概要
トークンに関する情報を扱うエンドポイント

### URL
- POST /token

#### パラメータ

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| email      | ○    | string | メールアドレス |
| password   | ○    | string | パスワード |

### Response

Status: 200 OK

```josn
{
  "token": "token"
  "user_id": "user_id"
}
```