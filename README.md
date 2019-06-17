# Repo的設計目標

使學員能夠在本地端使用Docker理解 RDB與 DynamoDB的操作，並能使用Jupyter提供的Python環境，針對資料庫進行連線。

## 資料夾結構
```
cxcxc_db_tutorial/
	docker-compose.yml  (含mysql、dynamoDB與Jupyter的類開發環境)
	mysql-basic-tutorial （RDB, MySQL的經典核心指令）
	
```

## RDB

面對資料庫三大要素、Database, Table, Item, 進行核心功能的流程展示

創建資料庫 ->  創建表格 -> 插入資料 -> 讀取資料 -> 更新資料 -> 備份資料庫 -> 刪除資料庫 -> 還原資料庫 -> 觀看DB Log
