from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector as mysql
root=Tk()
root.geometry("1500x900")
root.resizable(0,0)
root.config(bg="#4785CF")
root.title("Sign Up Page")
#signup widgets including labels entry fields and buttons

# Create users account with the information provided by users which can be finally used for login purposes
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


# create image inside the label as background
image2=Image.open("tourMainBgSignup.png")
image_resize=image2.resize((850,700))
converted1=ImageTk.PhotoImage(image_resize)
label2=Label(root,image=converted1,bd=0,bg="#4785CF")
label2.place(x=580,y=50)

# background image is set for entries and labels for the signup purposes
image1=PhotoImage(file="backgroundEntry.png")
label1=Label(root,image=image1,bg="#4785CF",bd=0)
label1.place(x=30,y=130)

# image of plane is placed
imageLogo=Image.open("flig.png")
imageResize=imageLogo.resize((60,60))
convertedOne=ImageTk.PhotoImage(imageResize)
label3=Label(root,image=convertedOne,bd=0,bg="#4785CF")
label3.place(x=60,y=20)

travel_label=Label(root,text="TOUR AND TRAVEL PVT.LTD",font=("Arial",22,"bold"),bg="#4785CF")
travel_label.place(x=150,y=32)

create_label=Label(label1,text="Create Account Now",font=("Arial",20,"bold"),fg="blue", bg = "#FFF")
create_label.place(x=300,y=40)

def labelEntries(text,x,y):   # create function to place different labels for the efficiency
     #of code passing parameters and arguments 
    label=Label(label1,text=text,bd=0,bg="white", font = ('Aerial', 14))
    label.place(x=x,y=y)

labels = []

labelEntries("Name •",164,139)
labelEntries("Email •",170,238)
labelEntries("Contact No •",164,338)
labelEntries("Address •",164,436)
labelEntries("Username •",570,139)
labelEntries("Confirm Password •",570,338)
labelEntries("Password •",570,238)

label_log=Label(label1,text="Already have an account?",font=24,fg="blue")
label_log.place(x=300,y=570)


# create entries for filling details
name_entry=Entry(label1,width=27,bd=0,bg="#d6d6d6", font = ('Tahoma', 12))
name_entry.place(x=98,y=174,height=38)
email_entry=Entry(label1,width=27,bd=0,bg="#d6d6d6", font = ('Tahoma', 12))
email_entry.place(x=98,y=270,height=38)
contact_var=StringVar()
contact_entry=Entry(label1,width=27,bd=0,bg="#d6d6d6", font = ('Tahoma', 12),textvariable=contact_var)
contact_entry.place(x=98,y=369,height=38)
address_var=StringVar()
address_entry=Entry(label1,width=27,bd=0,bg="#d6d6d6", font = ('Tahoma', 12),textvariable=address_var)
address_entry.place(x=98,y=464,height=38)

username_entry=Entry(label1,width=27,bd=0,bg="#d6d6d6", font = ('Tahoma', 12))
username_entry.place(x=508,y=179,height=38)
password_entry_var=StringVar()
password_entry=Entry(label1,width=27,bd=0,bg="#d6d6d6", font = ('Tahoma', 12),textvariable=password_entry_var,show="*")
password_entry.place(x=508,y=270,height=38)
confirm_password_entry_var=StringVar()
confirm_password_entry=Entry(label1,width=27,bd=0,bg="#d6d6d6", font = ('Tahoma', 12),textvariable=confirm_password_entry_var,show="*")
confirm_password_entry.place(x=508,y=369,height=38)


# create login function to display login interface
def login():
    root.destroy()
    import loginui
buttons=[]  # create empty buttons
def createbutton(text,x,y,cmd,font,bg,bd): # create function to create multiple buttons using code efficency
    button=Button(label1,text=text,command=cmd,font=font,bg=bg,bd=bd,relief=GROOVE,fg="#00FF00")
    button.place(x=x,y=y)
    buttons.append(button)  # append the each button inside the empty buttons
createbutton("CREATE",418,500,signup,76,"#FFF",2)
createbutton("Log in",545,570,login,12,"#FFF",0)

root.mainloop() 
