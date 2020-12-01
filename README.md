### 建立環境步驟

1. docker-compose up -d
2. mysql -h 172.19.0.1 -u testuser -p testdatabase < schemas/db_schema.sql(如果是用 sudo 起 docker 這邊也要加 sudo)
