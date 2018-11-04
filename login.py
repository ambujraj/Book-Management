from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import string
cur = sqlite3.connect('users.db')
c = cur.cursor()
root = Tk()
root.geometry('400x350')
root.resizable(False, False)
root.title("Login")
root.config(background="#1b9b6c")
username = 0
def register():
    root.destroy()
    os.system("python signup.py")
def avail():
    root.destroy()
    os.system("python availbook.py")
def auth():
    try:
        id = uid.get()
        passw = upass.get()
        abc = c.execute("SELECT regno,password FROM user WHERE regno= ? AND password= ?", (id, passw))
        for i in abc:
            if int(i[0]) == int(id) and str(i[1]) == str(passw):
                username=id
                avail()
                break


    except:
        messagebox.showinfo("Error!!","Username or Password not Valid!!")
    cur.close()
label_0 = Label(root,bg="black",fg="aqua", text="Login Here",width=20,font=("bold", 20))
label_0.place(x=40,y=53)
uid = IntVar()
label_2 = Label(root,bg="black",fg="white", text="Reg No.",width=10,font=("bold", 10))
label_2.place(x=25,y=120)
entry_2 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=uid)
entry_2.place(x=180,y=120)
upass = StringVar()
label_7 = Label(root,bg="black",fg="white", text="Password",width=10,font=("bold", 10))
label_7.place(x=25,y=160)
entry_7 = Entry(root, bd=5, bg="#44cfe2", fg="red",show="*", textvariable=upass)
entry_7.place(x=180,y=160)
Button(root, text='Login',width=20,bg='#4174f4',fg='white',command=auth).place(x=130,y=220)
Button(root, text='Register',width=20,bg='#525a5b',fg='white',command=register).place(x=130,y=260)
root.mainloop()
