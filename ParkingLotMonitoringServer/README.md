```sql
CREATE TABLE lot_status(
	id INT NOT NULL,
	isCar BOOLEAN NOT NULL DEFAULT 0,
	PRIMARY KEY(id)
)
mysql> explain lot_status
    -> ;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| id    | int        | NO   | PRI | NULL    |       |
| isCar | tinyint(1) | NO   |     | 0       |       |
+-------+------------+------+-----+---------+-------+
2 rows in set (0.01 sec)
```

mysql> explain lot_status;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| id    | int        | NO   | PRI | NULL    |       |
| isCar | tinyint(1) | NO   |     | 0       |       |
+-------+------------+------+-----+---------+-------+
2 rows in set (0.01 sec)