import mysql.connector as mql
import tkinter as tk
root = tk.Tk()
l1 = tk.Label(root, text = "username")
l1.grid(row = 0, column = 0)
t1 = tk.Entry(root)
t1.grid(row = 0, column=1)
l2 = tk.Label(root, text = "password")
l2.grid(row = 1, column = 0)
t2 = tk.Entry(root, show = "*")
t2.grid(row = 1, column=1)
def f1():
    mydb = mql.connect(
       host = "localhost",
       database = "mysql",
       user = t1.get(),
       password = t2.get()
    )
    print(mydb)
b1 = tk.Button(root, text = "Connect", command = f1)
b1.grid(row = 2, column = 0)










root.mainloop()