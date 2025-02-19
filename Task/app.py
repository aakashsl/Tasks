print("Starting the script...")

import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="3280151",
        database="testdb"
    )

    if conn.is_connected():
        print("Connected to MySQL successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
