# Userエンドポイント

## 目次
- [概要](#概要)
- [URL](#url)
  - [GET /user](#get-user)
  - [PUT /user](#put-user)
  - [DELETE /user](#delete-user)
  - [POST /user/signin](#post-usersignin)


## 概要
ユーザに関する情報を扱うエンドポイント

## URL
### GET /user

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| user_id    |      | string | ユーザID |
| token      | ○    | string | トークン |

### Response

Status: 200 OK

```json
{
  "user_info": {
    "user_id": "user_id",
    "name": "name",
    "email": "email",
    "icon_url": "icon_url",
    "twitter_url": "twitter_url",
    "facebook_url": "facebook_url",
    "instagram_url": "instagram_url",
    "linedin_url": "linedin_url",
    "school": "school",
    "Major": "Major",
    "rank": "rank",
  },
  "favorite_phrases": {
    {
      "phrase_id": "phrase_id",
      "phrase": "phrase",
      "likes": "likes",
    },
    {
      "phrase_id": "phrase_id",
      "phrase": "phrase",
      "likes": "likes",
    }
  },
  "login_history": {
    "2020-01-01": true,
    "2020-01-02": false,
    "2020-01-03": true,
    ...
  }
}
```

- ### PUT /user

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |
| name       |      | string | ユーザ名 |
| email      |      | string | メールアドレス |
| password   |      | string | パスワード |
| icon_url       |      | string（url） | アイコン |
| twitter_url    |      | string（url） | TwitterのURL |
| facebook_url   |      | string（url） | FacebookのURL |
| instagram_url  |      | string（url） | InstagramのURL |
| linedin_url    |      | string（url） | LinedinのURL |

### Response 

Status: 200 OK

```json
{
  "user_id": "user_id",
  "name": "name",
  "email": "email",
  "icon_url": "icon_url",
  "twitter_url": "twitter_url",
  "facebook_url": "facebook_url",
  "instagram_url": "instagram_url",
  "linedin_url": "linedin_url"
}
```

- ### DELETE /user

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| token      | ○    | string | トークン |

### Response

Status: 200 OK

```json
{
    "message": "success to delete user"
}
```

- ### POST user/signup

| パラメータ | 必須 | 型 | 説明 |
|:-----------|:----:|:---|:-----|
| name       | △    | string | ユーザ名 |
| email      | ○    | string | メールアドレス |
| password   | ○    | string | パスワード |

### Response

```json
{
    "message": "success to signup"
}
```
