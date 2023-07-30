from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

display=Tk()
display.title("Book your tour with us")
display.geometry("1450x1450")
display.resizable(0,0)
# display.iconbitmap("a.ico")
display.config(bg="grey")
frame=Frame(display)
photo =Image.open("mainbg.jpg")
resized_image=photo.resize((1000,1000))
converted =ImageTk.PhotoImage(resized_image)
label= Label(display,image=converted,height=1000)
label.place(x=0,y=0)
frame1 = Frame(display,width=400,height=500,bg="grey",bd="7",relief=SUNKEN)
frame.place(x=1000,y=0)
frame.place(width=450,height=1000)

heading=Label(frame,text="SIGN UP FORM",font=("Arial",17,"bold"),fg="grey",bg="black").place(x=50,y=10)
first_name=Label(frame,text="First Name:",font=("Arial",15,"bold"))
first_name.place(x=30,y=50)
last_name=Label(frame,text="Last Name:",font=("Arial",15,"bold")).place(x=30,y=100)
d_o_b=Label(frame,text="Date of birth",font=("Arial",15,"bold")).place(x=30,y=150)
email=Label(frame,text="Email:",font=("Arial",15,"bold")).place(x=30,y=200)
address=Label(frame,text="Address:",font=("Arial",15,"bold")).place(x=30,y=250)
contact_no=Label(frame,text="Phone No:",font=("Arial",15,"bold")).place(x=30,y=300)
pass_word=Label(frame,text="Password:",font=("Arial",15,"bold")).place(x=30,y=350)
pass_word=Label(frame,text="Confirm Password:",font=("Arial",15,"bold")).place(x=30,y=400)
gender=Label(frame,text="Gender:",font=("arial",15,"bold")).place(x=30,y=450)
gender=StringVar()
gender.set(0)
radiobutton=Radiobutton(frame,text="male",value="male",var=gender)
radiobutton.place(x=250,y=450)
radiobutton1=Radiobutton(frame,text="female",value="female",var=gender)
radiobutton1.place(x=350,y=450)
def back():
    display.destroy()
    import Tour

def login():
    display.destroy()
    import log_in

def call():  #signup
    if name_entry.get()==""or x2.get()=="" or x4.get()=="" or x5.get()==""or x6.get()=="" or x7.get()=="" or x8.get()=="" or months.get()=="" or day.get()=="" or gender.get()=="":
        messagebox.showerror("error","Invalid input")
    else:
        messagebox.showinfo("success","Successfully signed up")
    display.destroy()
def func1(z):
    name_entry.delete(0,"end")
name_entry=Entry(frame)
name_entry.place(x=250,y=50)
name_entry.insert(0,"krishna")
name_entry.bind("<Enter>",func1)
def func2(z):
    if name_entry.get()=="":
        name_entry.insert(0,"krishna")
name_entry.bind("<FocusOut>",func2)

def func3(a):
    last_name_entry.delete(0,"end")
def func4(a):
    if last_name_entry.get()=="":
        last_name_entry.insert(0,"bhandari")
last_name_entry=Entry(frame)
last_name_entry.place(x=250,y=100)
last_name_entry.insert(0,"bhandari")
last_name_entry.bind("<FocusIn>",func3)
last_name_entry.bind("<FocusOut>",func4)
def func4(a):
    if last_name_entry.get()=="":
        last_name_entry.insert(0,"bhandari")

x3=Entry(frame).place(x=250,y=150)
months=StringVar()

combobox =ttk.Combobox(frame,textvariable=months,values=("jan","feb","march","april","may","june","july","august","september","october","november","december"),width=5,state="readonly")
combobox.place(x=250,y=150)
day=StringVar()
num=[]
for i in range(1,33):
    num.append(i)

combobox1 =ttk.Combobox(frame,textvariable=day,values=num,width=2,state="readonly")
combobox1.place(x=320,y=150)
year= StringVar()
spinbox = Spinbox(frame,textvariable=year,from_=1900,to_=2000,state="readonly",width=4)
spinbox.place(x=375,y=150)
x4_var=StringVar()
x4=Entry(frame,textvariable=x4_var)
x4.place(x=250,y=200)
x5_var=StringVar()
x5=Entry(frame,textvariable=x5_var)
x5.place(x=250,y=250)
x6_var=StringVar()
x6=Entry(frame,textvariable=x6_var)
x6.place(x=250,y=300)
password_entry_var=StringVar()
password_entry=Entry(frame,textvariable=password_entry_var,show="*")
password_entry.place(x=250,y=350)
confirm_password_entry_var=StringVar()
confirm_password_entry=Entry(frame,textvariable=confirm_password_entry_var,show="*")
confirm_password_entry.place(x=250,y=400)

signup_btn=Button(frame,text="Sign Up",font=("arial",15,"bold"),command=call)
signup_btn.place(x=175,y=490)
level=Label(frame,text="Already have an account?",font=("arial",10,"bold"))
level.place(x=153,y=570) 
login_btn=Button(frame,text="Login",font=("arial",15,"bold"),command=login)
login_btn.place(x=185,y=600)  
back_btn=Button(frame,text="back ",font=("arial",19,"bold"),fg="blue",command=back)
back_btn.place(x=185,y=650) 



display.mainloop()