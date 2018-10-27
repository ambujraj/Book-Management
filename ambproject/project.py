from tkinter import *
import webbrowser

def callback(event):
    webbrowser.open_new(r"C:\Users\coderguy\Desktop\abhipro\login.py")

root = Tk()
link = Label(root, text="LOGIN", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)

def callback(event):
    webbrowser.open_new(r"C:\Users\coderguy\Desktop\abhipro\Register.py")

root = Tk()
link = Label(root, text="REGISTER", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)

root=Tk()
root.geometry("400x100")
root.title("Home Page")
root.resizable(0,0)
but1=Button(root,text="login", bg="blue")
but2=Button(root,text="New User", bg="blue")
but3=Button(root,text="Available Books", bg="blue")
but1.grid(row=0,column=0, padx=10, ipadx=40, pady=40)
but2.grid(row=0,column=1, padx=10, ipadx=20, pady=40)
but3.grid(row=0,column=2, padx=10, ipadx=10, pady=40)
root.mainloop()