import mysql.connector as mql
import tkinter as tk


mydb = mql.connect(
    host = "localhost",
    database = "mysql",
    user = "root",
    password = "4JVkrk75Jamd"
    
)
print("Data connected successfuly.")
cursor = mydb.cursor()
sql = "create database employee"
cursor.execute(sql)
mydb.close()
print("Database created successfully.")