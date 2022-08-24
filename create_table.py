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
sql = "create table employees (id int, emp_name varchar(20), emp_phone int(10), emp_sal int(10));"

cursor.execute(sql)
mydb.close()
print("Table created successfully.")

