from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()
def query_data(table):
    con=psycopg2.connect(
        host=os.getenv('db_host'),
        database=os.getenv('db_database'),
        user=os.getenv('db_user'),
        password=os.getenv('db_password'),
        port=5432
    )

    cur= con.cursor()
    query=f"select * from {table}"
    cur.execute(query)
    rows = cur.fetchall()
    con.close()
    return rows

def insert_data(prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3):

    con = psycopg2.connect(
        host=os.getenv('db_host'),
        database=os.getenv('db_database'),
        user=os.getenv('db_user'),
        password=os.getenv('db_password'),
        port=5432
    )
        
    cur = con.cursor()
    insert_query = f"""INSERT INTO jawad (prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3) 
        VALUES (%s, %s, %s, %s, %s, %s)"""
        
    cur.execute(insert_query, (prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3))
    con.commit()
    print("Record inserted successfully.")
