import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()
db_password = os.getenv('DB_PASSWORD')
dataBase = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd = db_password
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")