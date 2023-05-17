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
    "icon": "icon_url",
    "twitter": "twitter_url",
    "facebook": "facebook_url",
    "instagram": "instagram_url",
    "linedin": "linedin_url",
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
| icon       |      | string（url） | アイコン |
| twitter    |      | string（url） | Twitter |
| facebook   |      | string（url） | Facebook |
| instagram  |      | string（url） | Instagram |
| linedin    |      | string（url） | Linedin |

### Response 

Status: 200 OK

```json
{
  "user_id": "user_id",
  "name": "name",
  "email": "email",
  "icon": "icon_url",
  "twitter": "twitter_url",
  "facebook": "facebook_url",
  "instagram": "instagram_url",
  "linedin": "linedin_url"
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
| name       | ○    | string | ユーザ名 |
| email      | ○    | string | メールアドレス |
| password   | ○    | string | パスワード |

### Response

```json
{
    "message": "success to signup"
}
```
