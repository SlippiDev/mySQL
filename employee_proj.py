from email import message
from pickletools import long4
from re import L
from tkinter import messagebox
import mysql.connector as mql
import tkinter as tk
from tkinter import ttk

def add():
    emp_id = e1.get()
    emp_name = e2.get()
    emp_phone = e3.get()
    emp_sal = e4.get()

    mydb = mql.connect(
    host = "localhost",
    database = "employee",
    user = "root",
    password = "4JVkrk75Jamd"
    
        )
    print("Data connected successfuly.")
    cursor = mydb.cursor()
    sql = "insert into employees (id, emp_name, emp_phone, emp_sal) values (%s,%s,%s,%s)"
    val = (emp_id, emp_name, emp_phone, emp_sal)
    cursor.execute(sql, val)
    mydb.commit() 
    mydb.close()
    print("Data inserted successfully.")
    messagebox.showinfo("Information", "Employee Inserted Successfully...")
    show()
def show():
    mydb = mql.connect(
    host = "localhost",
    database = "employee",
    user = "root",
    password = "4JVkrk75Jamd"
    
    )
    print("Data connected successfuly.")
    cursor = mydb.cursor()
    sql = "select * from employees"

    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    mydb.close()
    print("Data shown successfully.")
def delete():
    emp_id = e1.get()
    mydb = mql.connect(
    host = "localhost",
    database = "employee",
    user = "root",
    password = "4JVkrk75Jamd"
    
    )
    print("Data connected successfuly.")
    cursor = mydb.cursor()
    sql = "delete from employees where id = %s"
    val = (emp_id,)
    cursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Information", "Record Deleted Successfully...")
    show()
def searchid():
    emp_id = e1.get()
    mydb = mql.connect(
    host = "localhost",
    database = "employee",
    user = "root",
    password = "4JVkrk75Jamd"
    
    )
    print("Data connected successfuly.")
    cursor = mydb.cursor()
    sql = "select id, emp_name, emp_phone, emp_sal from employees where id = %s"
    val = (emp_id,)
    cursor.execute(sql, val)
    records = cursor.fetchall()
    e2.insert(0, records[0][1])
    e3.insert(0, records[0][2])
    e4.insert(0, records[0][3]) # discuss
    print(records)
    messagebox.showinfo("Information", "Records Found")
root = tk.Tk()
root.geometry("800x500")
l1 = tk.Label(root, text = "REGISTRATION FORM", font = ("Times", 14, "bold", "underline"))
l1.place(x = 300, y = 5)

l2 = tk.Label(root, text = "Employee ID").place(x = 10, y = 50)

e1 = tk.Entry(root)
e1.place(x = 140, y = 50)

l3 = tk.Label(root, text = "Employee Name").place(x = 10, y = 90)

e2 = tk.Entry(root)
e2.place(x = 140, y = 90)

l4 = tk.Label(root, text = "Mobile Number").place(x = 10, y = 130)

e3 = tk.Entry(root)
e3.place(x = 140, y = 130)

l5 = tk.Label(root, text = "Salary").place(x = 10, y = 170)

e4 = tk.Entry(root)
e4.place(x = 140, y = 170)

b1 = tk.Button(root, text = "Add", command = add, height=1, width=15).place(x = 30, y = 210)

b2 = tk.Button(root, text = "Delete", command = delete, height=1, width=15).place(x=30, y= 250)

b3 = tk.Button(root, text = "Search by ID", command = searchid, height=1, width=15).place(x=30, y= 290)


root.mainloop()