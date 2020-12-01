### Introduction

* 由於簡化測試流程，所以這次只用 sqlite 做開發，下一個 header 是原本預期的環境架設
* 另外因為用 memory 做測試用，所以 url_to_hash 才需要帶入 db 參數以方便單元測試可以自建資料
* 更進一步的實作應該要加上 cache，減少一些熱門 url 打資料庫的次數
* 測試步驟: python3 test_shorten_url.py

### 預期建立環境步驟

1. docker-compose up -d
2. mysql -h 172.19.0.1 -u testuser -p testdatabase < schemas/db_schema.sql(如果是用 sudo 起 docker 這邊也要加 sudo)
