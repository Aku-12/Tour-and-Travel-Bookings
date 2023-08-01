from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root=Tk()
root.geometry("1300x900")
root.resizable(0,0)
root.config(bg="#4785CF")
root.title("Sign Up Page")
#signup widgets including labels entry fields and buttons

create_label=Label(root,text="CREATE ACCOUNT",font=("Arial",23,"bold"),fg="blue")
create_label.place(x=200,y=100)
image=Image.open("tourMainBg.png")
image_resize=image.resize((700,700))
converted=ImageTk.PhotoImage(image_resize)
label=Label(root,image=converted,bd=0,bg="#4785CF")
label.place(x=580,y=50)
image1=PhotoImage(file="signup.png")
label=Label(root,image=image1,bg="#4785CF",bd=0)
label.place(x=30,y=100)
def label1(text,x,y):
    label=Label(root,text=text,font=75,bd=0,bg="white")
    label.place(x=x,y=y)

label1("Name •",150,220)
label1("Email •",150,330)
label1("Contact No •",150,440)
label1("Address •",150,550)
label1("Password •",520,220)
label1(" Confirm Password •",520,445)
label1("Password •",520,330)

label_log=Label(root,text="Already have an account?",font=24,fg="blue")
label_log.place(x=580,y=660)
entrylist=[]
def create_entry(x,y):
    entry=Entry(root,width=43,bd=0,bg="#D9D9D9")
    entry.place(x=x,y=y,height=43)
    entrylist.append(entry)
create_entry(135,262)
create_entry(135,372)
create_entry(135,482)
create_entry(135,592)
create_entry(510,262)
create_entry(510,379)
create_entry(510,497)

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
    button=Button(root,text=text,command=cmd,font=font,bg=bg,bd=0)
    button.place(x=x,y=y)
    buttons.append(button)
createbutton("CREATE",365,660,signup,76,"#CDC0B0")
createbutton("Log in",622,690,login,12,"#D9D9D9")




root.mainloop()