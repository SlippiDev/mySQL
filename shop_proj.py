import mysql.connector as mql
import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
l1 = tk.Label(root, text = "ITEM STOCK", font = ("Times", 14, "bold", "underline"))
l1.place(x = 300, y = 5)

l2 = tk.Label(root, text = "Item Name").place(x = 10, y = 50)

e1 = tk.Entry(root).place(x = 140, y = 50)

l3 = tk.Label(root, text="Item ID").place(x=10, y = 90)

e2 = tk.Entry(root).place(x=140, y=90)

l4 = tk.Label(root, text = "Item Status").place(x=10, y = 130)

e3 = tk.Entry(root).place(x = 140, y = 130)

l5 = tk.Label(root, text = "Item Quantity").place(x = 10, y = 170)

e4 = tk.Entry(root).place(x = 140, y = 170)















root.mainloop()