# 基本操作

個人的には、[コンテナをバックグランドで起動](#コンテナを起動)して、[コンテナに入って作業](#コンテナに入る)する方法でいつも作業している。

## ビルドファイルを作成
    
```bash
docker compose build
```

## コンテナを起動

```bash
docker compose up -d
```

## コンテナに入る

```bash
docker compose exec app sh
```
※alpineなので、bashではなくsh

## コンテナを停止

```bash
docker compose down
```

## 一時的にコンテナ内でコマンドを実行（テストなどでよく使うイメージ）

```bash
docker compose run -rm app sh -c "python manage.py startapp app"
```

