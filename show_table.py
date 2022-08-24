import mysql.connector as mql
import tkinter as tk


mydb = mql.connect(
    host = "localhost",
    database = "employee",
    user = "root",
    password = "4JVkrk75Jamd"
    
)
print("Data connected successfuly.")
cursor = mydb.cursor()
sql = "show tables;"

cursor.execute(sql)
result = cursor.fetchall()
for i in result:
    print(i)
mydb.close()
print("Table shown successfully.")

