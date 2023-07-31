from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as mysql

display=Tk()
display.title("Book your tour with us")
display.geometry("1450x1450")
display.resizable(0,0)
# display.iconbitmap("a.ico")
display.config(bg="grey")
def signup():
    name1 = name_entry.get()
    username1 = username_entry.get()
    email1= email_entry.get()
    address1 = address_entry.get()
    contact_no1 = contact_entry.get()
    password = password_entry.get()
    con = mysql.connect(host="localhost",user="root",password="12345",database="signup")
    cursor = con.cursor()
    cursor.execute('INSERT INTO user VALUES("'+name1+'","'+ username1 +'","'+ email1 +'","'+ address1 +'","'+ contact_no1 +'","'+password+'")')
    if password_entry.get()==confirm_password_entry.get():
        if name1=="" or username1 == "" or email1=="" or address1=="" or contact_no1=="" or password=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            messagebox.showinfo("Success","Created account Successfully")
    else:
        messagebox.showerror("Error","password mismatched")

    con.commit()
    con.close()


frame=Frame(display)
photo =Image.open("everest1.png")
resized_image=photo.resize((1000,1000))
converted =ImageTk.PhotoImage(resized_image)
label= Label(display,image=converted,height=1000)
label.place(x=0,y=0)
frame1 = Frame(display,width=400,height=500,bg="grey",bd="7",relief=SUNKEN)
frame.place(x=1000,y=0)
frame.place(width=450,height=1000) 

heading=Label(frame,text="SIGN UP FORM",font=("Arial",17,"bold"),fg="grey",bg="black").place(x=50,y=10)
name=Label(frame,text="Name",font=("Arial",15,"bold"))
name.place(x=30,y=50)
username =Label(frame,text="Username",font=("Arial",15,"bold"))
username.place(x=30,y=100)
email=Label(frame,text="Email:",font=("Arial",15,"bold")).place(x=30,y=150)
address=Label(frame,text="Address:",font=("Arial",15,"bold")).place(x=30,y=200)
contact_no=Label(frame,text="Contact No:",font=("Arial",15,"bold")).place(x=30,y=250)
pass_word=Label(frame,text="Password:",font=("Arial",15,"bold")).place(x=30,y=300)
pass_word=Label(frame,text="Confirm Password:",font=("Arial",15,"bold")).place(x=30,y=350)

def back():
    display.destroy()
    import Tour

def login():
    display.destroy()
    import loginui

def call():  #signup
    if name_entry.get()==""or username_entry.get()=="" or email_entry.get()=="" or address_entry.get()==""or contact_entry.get()=="" or password_entry.get()=="" or confirm_password_entry.get()=="":
        messagebox.showerror("error","Invalid input")
    else:
        messagebox.showinfo("success","Successfully signed up")
    display.destroy()
def func1(z):
    name_entry.delete(0,"end")
name_entry=Entry(frame,width=22)
name_entry.place(x=250,y=50)
username_entry=Entry(frame,width=22)
username_entry.place(x=250,y=100)

email_entry=Entry(frame,width=22)
email_entry.place(x=250,y=150)
address_var=StringVar()
address_entry=Entry(frame,width=22,textvariable=address_var)
address_entry.place(x=250,y=200)
contact_var=StringVar()
contact_entry=Entry(frame,width=22,textvariable=contact_var)
contact_entry.place(x=250,y=250)
password_entry_var=StringVar()
password_entry=Entry(frame,width=22,textvariable=password_entry_var,show="*")
password_entry.place(x=250,y=300)
confirm_password_entry_var=StringVar()
confirm_password_entry=Entry(frame,width=22,textvariable=confirm_password_entry_var,show="*")
confirm_password_entry.place(x=250,y=350)

signup_btn=Button(frame,text="Sign Up",font=("arial",15,"bold"),command=signup)
signup_btn.place(x=175,y=400)
level=Label(frame,text="Already have an account?",font=("arial",10,"bold"))
level.place(x=153,y=450) 
login_btn=Button(frame,text="Login",font=("arial",15,"bold"),command=login)
login_btn.place(x=185,y=480)  
back_btn=Button(frame,text="back ",font=("arial",19,"bold"),fg="blue",command=back)
back_btn.place(x=185,y=530) 



display.mainloop()