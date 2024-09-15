from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()

# Function to query data from the database
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

        cur = con.cursor()

        # Prepare and execute the SQL query
        query = f"SELECT * FROM {table}"
        cur.execute(query)

        # Fetch all rows
        rows = cur.fetchall()

        # Return the fetched rows
        return rows

    except Exception as e:
        print(f"An error occurred while querying data: {e}")

    finally:
        # Always ensure the connection is closed
        if con:
            cur.close()
            con.close()

# Function to insert or update data in the database
def insert_data(prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3):
    """
    Inserts or updates a record in the 'jawad' table.
    
    :param prescription_name: Name of the prescription
    :param raw_instruction: Instructions for the prescription
    :param expiration_date: Expiration date of the prescription
    :param expected_time1: First expected time for the prescription
    :param expected_time2: Second expected time for the prescription
    :param expected_time3: Third expected time for the prescription
    """
    try:
        # Connect to the database
        con = psycopg2.connect(
            host=os.getenv('db_host'),
            database=os.getenv('db_database'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            port=5432
        )
        
        cur = con.cursor()

        # SQL query for inserting or updating the record, with placeholders for safety
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
        
        # Convert empty strings to None so that NULL is inserted in the database
        expected_time1 = expected_time1 if expected_time1 else None
        expected_time2 = expected_time2 if expected_time2 else None
        expected_time3 = expected_time3 if expected_time3 else None

        # Execute the insert or update query with the provided column values
        cur.execute(insert_query, (prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3))
        con.commit()

        print("Record inserted/updated successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the cursor and the connection
        if cur:
            cur.close()
        if con:
            con.close()
