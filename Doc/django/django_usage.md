# 初めに確認してほしいこと

### スーパーユーザを作成して、Adminサイトを確認する

1. スーパーユーザを作成する

```bash
$ python manage.py createsuperuser
```

2. adminページを開いて、データベースの内容を見れるかを確認する
※ログインするためのユーザを作成する必要がある（1番のコマンドでスーパーユーザを作っている場合、それでログインできる！！）

[Adminサイト](http://localhost:8000/admin)

# Djangoのよく使うコマンド

## アプリの作成

```bash
$ python manage.py startapp <app_name>
```

## マイグレーションファイルの作成

```bash
$ python manage.py makemigrations
```

## マイグレーション

```bash
$ python manage.py migrate
```
## スーパーユーザーの作成

```bash
$ python manage.py createsuperuser
```

## Djangoシェルの起動

```bash
$ python manage.py shell
```

