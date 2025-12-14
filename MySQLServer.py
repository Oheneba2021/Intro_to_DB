import mysql.connector

Intro_to_DB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "962!%628E=EiM}Rgkap",
    database = "alx_book_store"
)

print(Intro_to_DB.server_info)

mycursor = Intro_to_DB.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")

print("Database 'alx_book_store' created successfully!")