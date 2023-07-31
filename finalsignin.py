from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root=Tk()
root.geometry("1300x900")
root.resizable(0,0)
root.config(bg="#4785CF")
root.title("Sign Up Page")
#signup widgets including labels entry fields and buttons

image=Image.open("tourMainBg.png")
image_resize=image.resize((700,700))
converted=ImageTk.PhotoImage(image_resize)
label=Label(root,image=converted,bd=0,bg="#4785CF")
label.place(x=580,y=50)
image1=PhotoImage(file="signup.png")
label=Label(root,image=image1,bg="#4785CF",bd=0)
label.place(x=30,y=100)
def label1(text,x,y):
    label=Label(root,text=text,font=29)
    label.place(x=x,y=y)

label1("Name •",130,240)
label1("Email •",130,240)
label1("Contact No •",130,240)
label1("Address •",130,240)
label1("Password •",130,240)
label1(" Confirm Password •",130,240)
entrylist=[]
def create_entry(x,y):
    entry=Entry(root,width=24,bd=0)
    entry.place(x=x,y=y,heigh=39)
    entrylist.append(entry)
create_entry(110,272)
create_entry(110,372)
create_entry(110,470)
create_entry(480,272)
create_entry(480,372)
create_entry(480,463)
def login():
    root.destroy()
    import finalsignin
def signup():
    if entrylist[0]=="" or entrylist[0]=="" or entrylist[1]=="" or entrylist[2]=="" or entrylist[3]=="" or entrylist[4]=="":
        messagebox.showerror("Error","Entry fields required")
    else:
        messagebox.showinfo("Successfully signed up")
buttons=[]
def createbutton(text,x,y,cmd,font,bg):
    button=Button(root,text=text,command=cmd,font=font,bg=bg)
    button.place(x=x,y=y)
    buttons.append(button)
createbutton("CREATE",358,557,signup,76,"blue")
createbutton("Log in",475,620,login,12,"blue")




root.mainloop()