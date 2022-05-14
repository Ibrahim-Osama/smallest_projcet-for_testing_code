from tkinter import *
import tkinter.messagebox as m
import mysql.connector
my = mysql.connector.connect(  
host  = "localhost",
user = "root",
password = "",
database = "app")
def insetrdata():
    mycursorObject=my.cursor()
    username = e1.get()
    Querycode = f"INSERT INTO users(username)VALUES('{username}')"
    mycursorObject.execute(Querycode)
    my.commit()
def updatedata():
    mycursorObject=my.cursor()
    username = e2.get()
    Querycode = f"UPDATE users SET users.username = '{username}'"
    mycursorObject.execute(Querycode)
    my.commit()
def deletedata():
    mycursorObject=my.cursor()
    Querycode = f"DELETE FROM users"
    mycursorObject.execute(Querycode)
    my.commit()
    
w = Tk()
w.title(string='Simple Calc')
w.geometry('300x400')
label1 = Label(w,text=' Welcome To Dashboard')
label1.pack()
label1.configure(font=("Courier", 16, "italic"))
e1 = Entry(w , fg='red')
e1.pack(pady=5)
b2 = Button( w, text='Insert'  ,bg='green',fg='white' ,command=insetrdata )
b2.pack(pady=5)
b3 = Button( w, text='Delete'  ,bg='green',fg='white' ,command=deletedata)
b3.pack()
e2 = Entry(w , fg='red')
e2.pack(pady=5)
b4 = Button( w, text='Update'  ,bg='green',fg='white',command= updatedata )
b4.pack()
w.mainloop()