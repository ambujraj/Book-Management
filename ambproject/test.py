from tkinter import *
from tkinter import messagebox
import sqlite3
import string

cur = sqlite3.connect('users.db')
c = cur.cursor()
abc=c.execute("select regno,password from user where regno=? and password=?",(11703203, "Qwerty143"))
info = abc.fetchone()
for i in info:
    print(i)