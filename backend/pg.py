from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()

con=psycopg2.connect(
    host=os.getenv('db_host'),
    database=os.getenv('db_database'),
    user=os.getenv('db_user'),
    password=os.getenv('db_password'),
    port=5432
)

cur= con.cursor()
cur.execute("select * from pub")
rows = cur.fetchall()
for row in rows:
        print(row)
con.close()