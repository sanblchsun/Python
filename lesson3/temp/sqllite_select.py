
import sqlite3

conn = sqlite3.connect("C:\\Users\\JavaCode\\Desktop\\1\\tiles.sqlite")
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()
sql = "select * \
from information_schema.columns \
where table_schema='public'"
for row in cursor.execute(sql):
    print(row)