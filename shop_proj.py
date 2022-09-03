from tkinter import messagebox
import mysql.connector as mql
import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
# sql functions
def getvalue():
    global item_id
    global item_name
    global item_status
    item_name = e1.get()
    item_id = e2.get()
    item_status = e3.get()
def add():
    getvalue()
    mydb = mql.connect(
    host = "localhost",
    database = "shopkeeper",
    user = "root",
    password = "4JVkrk75Jamd"
    )

    cursor = mydb.cursor()

    sql = "insert into items values(%s, %s, %s)"
    val = (item_name, item_id, item_status)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
# tkinter
    messagebox.showinfo("Information", "Added Record")
l1 = tk.Label(root, text = "ITEM STOCK", font = ("Times", 14, "bold", "underline"))
l1.place(x = 300, y = 5)

l2 = tk.Label(root, text = "Item Name").place(x = 10, y = 50)

e1 = tk.Entry(root)
e1.place(x = 140, y = 50)

l3 = tk.Label(root, text="Item ID").place(x=10, y = 90)

e2 = tk.Entry(root)
e2.place(x=140, y=90)

l4 = tk.Label(root, text = "Item Status").place(x=10, y = 130)

e3 = tk.Entry(root)
e3.place(x = 140, y = 130)

# buttons

b1 = tk.Button(root, text = "Add Item", command = add, height=1, width = 15).place(x = 10, y = 170)

















root.mainloop()