from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()

def query_data(table):
    try:
        # Connect to the database
        con = psycopg2.connect(
            host=os.getenv('db_host'),
            database=os.getenv('db_database'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            port=5432
        )
        #query stuff
        cur = con.cursor()
        query = f"SELECT * FROM {table}"
        cur.execute(query)

        rows = cur.fetchall()
        return rows
    
        #error handling
    except Exception as e:
        print(f"An error occurred while querying data: {e}")

    finally:
        if con:
            cur.close()
            con.close()

def insert_data(prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3):
    try:
        #Connect to the database
        con = psycopg2.connect(
            host=os.getenv('db_host'),
            database=os.getenv('db_database'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            port=5432
        )
        
        cur = con.cursor()
        insert_query = """
            INSERT INTO jawad (prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3) 
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (prescription_name) 
            DO UPDATE SET 
                raw_instruction = EXCLUDED.raw_instruction,
                expiration_date = EXCLUDED.expiration_date,
                expected_time1 = EXCLUDED.expected_time1,
                expected_time2 = EXCLUDED.expected_time2,
                expected_time3 = EXCLUDED.expected_time3;
        """
        
        expected_time1 = expected_time1 if expected_time1 else None
        expected_time2 = expected_time2 if expected_time2 else None
        expected_time3 = expected_time3 if expected_time3 else None
        cur.execute(insert_query, (prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3))
        con.commit()

        print("Record inserted/updated successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        #Close the cursor and the connection
        if cur:
            cur.close()
        if con:
            con.close()