from tkinter import *
from tkinter import messagebox
import sqlite3
from backend import db
import string
import os
curr = sqlite3.connect('users.db')
c = curr.cursor()
database = db()
c.execute("CREATE TABLE IF NOT EXISTS user(regno INTEGER PRIMARY KEY, name TEXT, address TEXT, gender TEXT, mobile TEXT, email TEXT, password TEXT)")
curr.commit()
root = Tk()
root.geometry('230x80')
root.resizable(False, False)
root.title("HomePage")
root.config(background="#1b9b6c")
def login():
    root.destroy()
    os.system("python login.py")
def signup():
    root.destroy()
    os.system("python signup.py")

Button(root, text='Login', width=15, bg='#4174f4', fg='white',command=login).grid(row=1,column=1)
Button(root, text='Register', width=15, bg='#4174f4', fg='white',command=signup).grid(row=1,column=2)

root.mainloop()
