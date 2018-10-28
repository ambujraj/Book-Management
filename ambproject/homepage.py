from tkinter import *
from tkinter import messagebox
from backend import db
import sqlite3
import string
cur = sqlite3.connect('users.db')
c = cur.cursor()
database = db()
valid = 0
def signup():
    root = Tk()
    c.execute("CREATE TABLE IF NOT EXISTS user(regno INTEGER PRIMARY KEY, name TEXT, address TEXT, gender TEXT, mobile TEXT, email TEXT, password TEXT)")
    cur.commit()
    root.geometry('500x650')
    root.title("Create Account")
    root.config(background="#1b9b6c")

    # start Validation
    def validmob():
        x = e4.get()
        if (len(x) == 10 and x.isdigit()):
            validpass()
        else:
            messagebox.showinfo("Invalid Entry!!", "Mobile number should be 10 digits")

    def validpass():
        x1 = e6.get()
        x2 = e7.get()
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
                messagebox.showinfo("Invalid Entry!!",
                                    "Passwords should contain atleast 1 lowercase, 1 uppercase, 1 digit!!")
        else:
            messagebox.showinfo("Invalid Entry!!",
                                "Passwords not valid!!\nNote: Password should be between 6 to 10 letters")

    def validreg():
        x3 = str(e2.get())
        if (len(x3) == 8):
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
            c.execute("INSERT INTO user(regno,name,address,gender,mobile,email,password) VALUES(?,?,?,?,?,?,?)",
                      (regid, name, add, gender, mob, email, passw))
            messagebox.showinfo("Success!!", "Account Successfully Created!!\nNow Please Login")
        except:
            messagebox.showinfo("Error", "Registration Number already registered, try logging in!!")
        cur.commit()
        cur.close()

    e1 = StringVar()
    e2 = IntVar()
    e3 = StringVar()
    e4 = StringVar()
    e5 = StringVar()
    e6 = StringVar()
    e7 = StringVar()
    label_0 = Label(root, bg="black", fg="aqua", text="Register Here", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(root, bg="black", fg="white", text="Name", width=10)
    label_1.place(x=70, y=130)
    entry_1 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=e1)
    entry_1.place(x=240, y=130)
    label_2 = Label(root, bg="black", fg="white", text="Reg no.", width=10)
    label_2.place(x=70, y=180)
    entry_2 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=e2)
    entry_2.place(x=240, y=180)
    label_3 = Label(root, bg="black", fg="white", text="Address", width=10)
    label_3.place(x=70, y=230)
    entry_3 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=e3)
    entry_3.place(x=240, y=230)
    label_4 = Label(root, bg="black", fg="white", text="Gender", width=10)
    label_4.place(x=70, y=280)
    v = StringVar()
    R1 = Radiobutton(root, bg="#1b9b6c", text="Male", variable=v, value="M")
    R1.place(x=235, y=280)
    R2 = Radiobutton(root, bg="#1b9b6c", text="Female", variable=v, value="F")
    R2.place(x=290, y=280)
    label_6 = Label(root, bg="black", fg="white", text="Mobile No", width=10)
    label_6.place(x=70, y=330)
    entry_6 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=e4)
    entry_6.place(x=240, y=330)
    label_7 = Label(root, bg="black", fg="white", text="Email", width=10)
    label_7.place(x=70, y=380)
    entry_7 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=e5)
    entry_7.place(x=240, y=380)
    label_8 = Label(root, bg="black", fg="white", text="Password", width=10)
    label_8.place(x=70, y=430)
    entry_8 = Entry(root, bd=5, bg="#44cfe2", fg="red", show="*", textvariable=e6)
    entry_8.place(x=240, y=430)
    label_9 = Label(root, bg="black", fg="white", text="Confirm Password", width=15, font=("bold", 10))
    label_9.place(x=70, y=480)
    entry_9 = Entry(root, bd=5, bg="#44cfe2", fg="red", show="*", textvariable=e7)
    entry_9.place(x=240, y=480)
    Button(root, text='REGISTER', width=50, bg='#2D39BF', fg='white', command=validmob).place(x=60, y=530)
    Button(root, text='LOGIN', width=50, bg='#2D39BF', fg='white',command=login).place(x=60, y=570)
    root.mainloop()

def login():
    root = Tk()
    root.geometry('400x350')
    root.title("Login")
    root.config(background="#1b9b6c")

    def auth():
        id = uid.get()
        passw = upass.get()

        try:
            abc = c.execute("SELECT regno,password FROM user WHERE regno= ? AND password= ?", (id, passw))
            for i in abc:
                if int(i[0]) == int(id) and str(i[1]) == str(passw):
                    valid=1
                    messagebox.showinfo("Success", "Successfully Logged In!!")
                    break

        except:
            messagebox.showinfo("Error!!", "Username or Password not Valid!!")
        cur.close()

    label_0 = Label(root, bg="black", fg="aqua", text="Login Here", width=20, font=("bold", 20))
    label_0.place(x=40, y=53)
    uid = IntVar()
    label_2 = Label(root, bg="black", fg="white", text="Reg No.", width=10, font=("bold", 10))
    label_2.place(x=25, y=120)
    entry_2 = Entry(root, bd=5, bg="#44cfe2", fg="red", textvariable=uid)
    entry_2.place(x=180, y=120)
    upass = StringVar()
    label_7 = Label(root, bg="black", fg="white", text="Password", width=10, font=("bold", 10))
    label_7.place(x=25, y=160)
    entry_7 = Entry(root, bd=5, bg="#44cfe2", fg="red", show="*", textvariable=upass)
    entry_7.place(x=180, y=160)
    Button(root, text='Login', width=20, bg='#4174f4', fg='white', command=auth).place(x=130, y=220)
    Button(root, text='Register', width=20, bg='#525a5b', fg='white',command=signup).place(x=130, y=260)
    root.mainloop()

def availb():
    if(valid==1):
        class Window(object):
            def __init__(self, window):
                self.window = window
                self.window.wm_title("Book Management System")

                l1 = Label(window, text="Book Name")
                l1.grid(row=0, column=0)

                l2 = Label(window, text="Author")
                l2.grid(row=0, column=2)

                l3 = Label(window, text="Year")
                l3.grid(row=1, column=0)

                l4 = Label(window, text="ISBN")
                l4.grid(row=1, column=2)

                self.title_text = StringVar()
                self.e1 = Entry(window, textvariable=self.title_text)
                self.e1.grid(row=0, column=1)

                self.author_text = StringVar()
                self.e2 = Entry(window, textvariable=self.author_text)
                self.e2.grid(row=0, column=3)

                self.year_text = StringVar()
                self.e3 = Entry(window, textvariable=self.year_text)
                self.e3.grid(row=1, column=1)

                self.ISBN_text = StringVar()
                self.e4 = Entry(window, textvariable=self.ISBN_text)
                self.e4.grid(row=1, column=3)

                self.list1 = Listbox(window, height=6, width=35)
                self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

                self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

                # scrollbar
                sb1 = Scrollbar(window)
                sb1.grid(row=2, column=2, rowspan=6)
                self.list1.config(yscrollcommand=sb1.set)
                sb1.config(command=self.list1.yview)

                b1 = Button(window, text="View all", width=12, command=self.view_command)
                b1.grid(row=2, column=3)

                b2 = Button(window, text="Search entry", width=12, command=self.search_command)
                b2.grid(row=3, column=3)

                b3 = Button(window, text="Add entry", width=12, command=self.add_command)
                b3.grid(row=4, column=3)
                b6 = Button(window, text="Close", width=12, command=window.destroy)
                b6.grid(row=5, column=3)

            # the "event" parameter is needed b/c we've binded this function to the listbox
            def get_selected_row(self,event):
                try:
                    index = self.list1.curselection()[0]
                    self.selected_tuple = self.list1.get(index)
                    self.e1.delete(0, END)
                    self.e1.insert(END, self.selected_tuple[1])
                    self.e2.delete(0, END)
                    self.e2.insert(END, self.selected_tuple[2])
                    self.e3.delete(0, END)
                    self.e3.insert(END, self.selected_tuple[3])
                    self.e4.delete(0, END)
                    self.e4.insert(END, self.selected_tuple[4])
                except IndexError:
                    pass  # in the case where the listbox is empty, the code will not execute

            def view_command(self):
                self.list1.delete(0,
                                  END)  # make sure we've cleared all entries in the listbox every time we press the View all button
                for row in database.view():
                    self.list1.insert(END, row)

            def search_command(self):
                self.list1.delete(0, END)
                for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                           self.ISBN_text.get()):
                    self.list1.insert(END, row)

            def add_command(self):
                database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
                self.list1.delete(0, END)
                self.list1.insert(END, (
                self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()))

            def delete_command(self):
                database.delete(self.selected_tuple[0])
                self.view_command()

            def update_command(self):
                # we are updating using the texts in the entries, not the selected tuple
                database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                self.ISBN_text.get())
                self.view_command()

        # code for the GUI (front end)
        window = Tk()
        Window(window)

        window.mainloop()
    else:
        messagebox.showinfo("Error","Please Login First!!")

root = Tk()
root.geometry('300x300')
root.title("HomePage")
root.config(background="#1b9b6c")
Button(root, text="Login", command=login).place(x=40,y=40)
Button(root, text="Register", command=signup).place(x=90,y=40)
Button(root, text="Available Books",command=availb).place(x=130,y=40)
root.mainloop()