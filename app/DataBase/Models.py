import sqlite3

db = sqlite3.connect("users_info.db")

cursor = db.cursor()
# cursor.execute(''' create table users(
#                 id int,
#                 user_id text,
#                 balance int,
#                 number int
#                )''')

db.commit()
db.close()
