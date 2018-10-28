from tkinter import *
from tkinter import messagebox
import sqlite3
from backend import db

class mainUI(Frame):
    def login(self):
        self.controller.show_frame("LoginFrame")
    def register(self):
        self.controller.show_frame("RegisterFrame")
    def availbook(self):
        self.controller.show_frame("AvailableBooks")
    def __init__(self,parent,controller):
        self.controller = controller
        Button(self, text="Login", command=self.login).grid(row=1, column=1, sticky='NE')
        Button(self, text="Register", command=self.register).grid(row=1, column=3, sticky='NE')
        Button(self, text="Available Books", command=self.availbook).grid(row=1, column=5, sticky='NE')

class RegisterFrame(Frame):
    def create_account(self):
        x = self.e4.get()
        if (len(x) == 10 and x.isdigit()):
            validpass()
        else:
            messagebox.showinfo("Invalid Entry!!", "Mobile number should be 10 digits")

        def validpass():
            x1 = self.e6.get()
            x2 = self.e7.get()
            p, q, r = 0, 0, 0
            if (x1 == x2 and 6 < len(x1) <= 10):
                for i in x1:
                    if (i.isupper()):
                        p = 1
                    if (i.islower()):
                        q = 1
                    if (i.isdigit()):
                        r = 1
                if (p == 1 and q == 1 and r == 1):
                    validreg()
                else:
                    messagebox.showinfo("Invalid Entry!!","Passwords should contain atleast 1 lowercase, 1 uppercase, 1 digit!!")
            else:
                messagebox.showinfo("Invalid Entry!!","Passwords not valid!!\nNote: Password should be between 6 to 10 letters")

        def validreg():
            x3 = str(self.e2.get())
            if (len(x3) == 8):
                add()
            else:
                messagebox.showinfo("Invalid Entry!!", "Registration no. not valid!!")

        def add():
            name = self.e1.get()
            regid = self.e2.get()
            add = self.e3.get()
            gender = self.v.get()
            mob = self.e4.get()
            email = self.e5.get()
            passw = self.e6.get()
            try:
                c.execute("INSERT INTO user(regno,name,address,gender,mobile,email,password) VALUES(?,?,?,?,?,?,?)",
                          (regid, name, add, gender, mob, email, passw))
                messagebox.showinfo("Success!!", "Account Successfully Created!!")
            except:
                messagebox.showinfo("Error", "Registration Number already registered, try logging in!!")
            self.cur.commit()
            self.cur.close()

        self.e1 = StringVar()
        self.e2 = IntVar()
        self.e3 = StringVar()
        self.e4 = StringVar()
        self.e5 = StringVar()
        self.e6 = StringVar()
        self.e7 = StringVar()


    def __init__(self,parent,controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.cur = sqlite3.connect("users.db")
        self.c = self.cur.cursor()
        root = Tk()
        root.geometry('500x650')
        root.title("Create Account")
        root.config(background="#1b9b6c")
        label_0 = Label(root, bg="black", fg="aqua", text="Register Here", width=20, font=("bold", 20))
        label_0.place(x=90, y=53)
        label_1 = Label(root, bg="black", fg="white", text="Name", width=10)
        label_1.place(x=70, y=130)
        entry_1 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=self.e1)
        entry_1.place(x=240, y=130)
        label_2 = Label(root, bg="black", fg="white", text="Reg no.", width=10)
        label_2.place(x=70, y=180)
        entry_2 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=self.e2)
        entry_2.place(x=240, y=180)
        label_3 = Label(root, bg="black", fg="white", text="Address", width=10)
        label_3.place(x=70, y=230)
        entry_3 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=self.e3)
        entry_3.place(x=240, y=230)
        label_4 = Label(root, bg="black", fg="white", text="Gender", width=10)
        label_4.place(x=70, y=280)
        self.v = StringVar()
        R1 = Radiobutton(root, bg="#1b9b6c", text="Male", variable=self.v, value="M")
        R1.place(x=235, y=280)
        R2 = Radiobutton(root, bg="#1b9b6c", text="Female", variable=self.v, value="F")
        R2.place(x=290, y=280)
        label_6 = Label(root, bg="black", fg="white", text="Mobile No", width=10)
        label_6.place(x=70, y=330)
        entry_6 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=self.e4)
        entry_6.place(x=240, y=330)
        label_7 = Label(root, bg="black", fg="white", text="Email", width=10)
        label_7.place(x=70, y=380)
        entry_7 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=self.e5)
        entry_7.place(x=240, y=380)
        label_8 = Label(root, bg="black", fg="white", text="Password", width=10)
        label_8.place(x=70, y=430)
        entry_8 = Entry(root, bd=5, bg="#44cfe2", fg="red", show="*", textvariable=self.e6)
        entry_8.place(x=240, y=430)
        label_9 = Label(root, bg="black", fg="white", text="Confirm Password", width=15, font=("bold", 10))
        label_9.place(x=70, y=480)
        entry_9 = Entry(root, bd=5, bg="#44cfe2", fg="red", show="*", textvariable=self.e7)
        entry_9.place(x=240, y=480)
        Button(root, text='REGISTER', width=50, bg='#2D39BF', fg='white', command=self.create_account).place(x=60, y=530)
        Button(root, text='LOGIN', width=50, bg='#2D39BF', fg='white',command=lambda: self.controller.show_frame("LoginFrame")).place(x=60, y=570)
        root.mainloop()

class LoginFrame(Frame):
        def auth(self):
            id = self.uid.get()
            passw = self.upass.get()
            try:
                abc = c.execute("SELECT regno,password FROM user WHERE regno= ? AND password= ?", (id, passw))
                for i in abc:
                    if int(i[0]) == int(id) and str(i[1]) == str(passw):
                        messagebox.showinfo("Success", "Successfully Logged In!!")
                        break
            except:
                messagebox.showinfo("Error!!", "Username or Password not Valid!!")
            cur.close()
        def __init__(self,parent,controller):
            Frame.__init__(self,parent)
            self.controller = controller
            self.cur = sqlite3.connect('users.db')
            self.c = self.cur.cursor()
            root = Tk()
            root.geometry('400x350')
            root.title("Login")
            root.config(background="#1b9b6c")
            self.label_0 = Label(root, bg="black", fg="aqua", text="Login Here", width=20, font=("bold", 20))
            self.label_0.place(x=40, y=53)
            self.uid = IntVar()
            self.label_2 = Label(root, bg="black", fg="white", text="Reg No.", width=10, font=("bold", 10))
            self.label_2.place(x=25, y=120)
            self.entry_2 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=self.uid)
            self.entry_2.place(x=180, y=120)
            self.upass = StringVar()
            self.label_7 = Label(root, bg="black", fg="white", text="Password", width=10, font=("bold", 10))
            self.label_7.place(x=25, y=160)
            self.entry_7 = Entry(root, bd=5, bg="#44cfe2", fg="red", show="*", textvariable=self.upass)
            self.entry_7.place(x=180, y=160)
            Button(root, text='Login', width=20, bg='#4174f4', fg='white', command=self.auth).place(x=130, y=220)
            Button(root, text='Register', width=20, bg='#525a5b', fg='white',command=lambda: self.controller.show_frame("RegisterFrame")).place(x=130, y=260)
            root.mainloop()


class SampleApp(Tk):
    def FrameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width = canvas_width)
    def __init__(self, *args, **kwargs):
        self.container = Frame(self.canvas)

        self.frames = {}

        self.show_frame("mainUI")

    def show_frame(self, page_name):
        frame = self.frames[page_name]

def main():
    app = SampleApp()
    app.mainloop()