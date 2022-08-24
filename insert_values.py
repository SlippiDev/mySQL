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
sql = "insert into employees (id, emp_name, emp_phone, emp_sal) values (%s,%s,%s,%s)"
val = ("1111", "Mark", "3458", "20000")
cursor.execute(sql, val)
mydb.commit()
mydb.close()
print("Data inserted successfully.")

