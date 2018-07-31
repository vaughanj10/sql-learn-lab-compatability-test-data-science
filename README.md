
# W.I.P. Learn/SQL QA


```python
# import sqlite3
# connection = sqlite3.connect('sports.db')
# cursor = connection.cursor()
# ---- or just the following: ----
# import connection, cursor from sql_runner
```


```python
# file = open('insert.sql')
# sql = file.read()
# cursor.executescript(sql)
```


```python
# add in 2 records to the leagues table
# ----- run this: -----
# file = open('insert_leagues.sql')
# sql = file.read()
# cursor.executescript(sql)
# ----- OR this: -----
# cursor.executescript('''INSERT INTO leagues (name) VALUES ("NHL"), ("NBA");''')
```
