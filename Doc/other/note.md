# データベースを初期化する
```
docker volume -rm <db-data>
docker-compose up -d
```

# コードを自動フォーマットする
```
docker compose exec app black <path>
```