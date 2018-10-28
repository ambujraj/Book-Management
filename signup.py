from tkinter import *
from tkinter import messagebox
import string
import sqlite3
import os
cur = sqlite3.connect('users.db')
c = cur.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(regno INTEGER PRIMARY KEY, name TEXT, address TEXT, gender TEXT, mobile TEXT, email TEXT, password TEXT)")
cur.commit()
root = Tk()
root.geometry('500x650')
root.title("Create Account")
root.config(background="#1b9b6c")
def login():
    root.destroy()
    os.system("python login.py")
#start Validation
def validmob():
    x = e4.get()
    if(len(x)==10 and x.isdigit()):
        validpass()
    else:
        messagebox.showinfo("Invalid Entry!!", "Mobile number should be 10 digits")
def validpass():
    x1 = e6.get()
    x2 = e7.get()
    p,q,r=0,0,0
    if(x1==x2 and 6<len(x1)<=10):
        for i in x1:
            if(i.isupper()):
               p=1
            if(i.islower()):
               q=1
            if(i.isdigit()):
                r=1
        if(p==1 and q==1 and r==1):
            validreg()
        else:
            messagebox.showinfo("Invalid Entry!!", "Passwords should contain atleast 1 lowercase, 1 uppercase, 1 digit!!")
    else:
        messagebox.showinfo("Invalid Entry!!", "Passwords not valid!!\nNote: Password should be between 6 to 10 letters")
def validreg():
    x3 = str(e2.get())
    if(len(x3)==8):
        add()
    else:
        messagebox.showinfo("Invalid Entry!!", "Registration no. not valid!!")
def add():
    name = e1.get()
    regid = e2.get()
    add = e3.get()
    gender = v.get()
    mob = e4.get()
    email = e5.get()
    passw = e6.get()
    try:
        c.execute("INSERT INTO user(regno,name,address,gender,mobile,email,password) VALUES(?,?,?,?,?,?,?)",(regid,name,add,gender,mob,email,passw))
        messagebox.showinfo("Success!!", "Account Successfully Created!!")
        login()
    except:
        messagebox.showinfo("Error","Registration Number already registered, try logging in!!")
    cur.commit()
    cur.close()

e1 = StringVar()
e2 = IntVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()
label_0 = Label(root,bg="black",fg="aqua", text="Register Here",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root,bg="black",fg="white", text="Name",width=10)
label_1.place(x=70,y=130)
entry_1 = Entry(root, bd=5, bg="#44cfe2", fg="red",textvariable=e1)
entry_1.place(x=240,y=130)
label_2 = Label(root,bg="black",fg="white", text="Reg no.",width=10)
label_2.place(x=70,y=180)
entry_2 = Entry(root, bd=5, bg="#44cfe2", fg="red",textvariable=e2)
entry_2.place(x=240,y=180)
label_3 = Label(root,bg="black",fg="white", text="Address",width=10)
label_3.place(x=70,y=230)
entry_3 = Entry(root, bd=5, bg="#44cfe2", fg="red",textvariable=e3)
entry_3.place(x=240,y=230)
label_4 = Label(root,bg="black",fg="white", text="Gender",width=10)
label_4.place(x=70,y=280)
v = StringVar()
R1 = Radiobutton(root,bg="#1b9b6c", text="Male", variable=v, value="M")
R1.place(x=235,y=280)
R2 = Radiobutton(root,bg="#1b9b6c", text="Female", variable=v, value="F")
R2.place(x=290,y=280)
label_6 = Label(root,bg="black",fg="white", text="Mobile No",width=10)
label_6.place(x=70,y=330)
entry_6 = Entry(root, bd=5, bg="#44cfe2", fg="red",textvariable=e4)
entry_6.place(x=240,y=330)
label_7 = Label(root,bg="black",fg="white", text="Email",width=10)
label_7.place(x=70,y=380)
entry_7 = Entry(root, bd=5, bg="#44cfe2", fg="red",textvariable=e5)
entry_7.place(x=240,y=380)
label_8 = Label(root,bg="black",fg="white", text="Password",width=10)
label_8.place(x=70,y=430)
entry_8 = Entry(root, bd=5, bg="#44cfe2", fg="red",show="*",textvariable=e6)
entry_8.place(x=240,y=430)
label_9 = Label(root,bg="black",fg="white", text="Confirm Password",width=15,font=("bold", 10))
label_9.place(x=70,y=480)
entry_9 = Entry(root, bd=5, bg="#44cfe2", fg="red", show="*",textvariable=e7)
entry_9.place(x=240,y=480)
Button(root, text='REGISTER',width=50,bg='#2D39BF',fg='white',command=validmob).place(x=60,y=530)
Button(root, text='LOGIN',width=50,bg='#2D39BF',fg='white',command=login).place(x=60,y=570)
root.mainloop()