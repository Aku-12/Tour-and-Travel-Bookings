from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.geometry("1400x1400")
root.resizable(0,0)
root.title("Admin Panel")
root.config(bg="#FFFACD")
label_roots=Label(root,text="Travel And Tour Booking System",font=("arial",29,"bold"),fg="orange",bg="#FFFACD")
label_roots.pack()
frame_all=Frame(root,width=1200,height=1000)


#destroy window to import loginpage when logout function is called
def logout():   
    
    root.destroy()
    import loginui
# save the data of users while editing user data when save function is called.
def save():
    name =name_entry.get()
    email =email_entry.get()
    address =address_entry.get()
    contact_no =contact_no_entry.get()
    try:
        if name_entry.get()=="" or username_entry1.get()=="" or email_entry.get()=="" or address_entry.get()=="" or contact_no_entry.get()=="":
            messagebox.showerror("error","All fields are required")
        else:
            # connecting UI with database using mysql
            con = mysql.connect(host='localhost', user='root',
                                password="12345", port="3306", database='signup')
            cursor = con.cursor()
            query_update = "update user set name =%s,email=%s,address=%s,contact_no=%s where username=%s"
            values = (name,email,address,contact_no,username1)
            cursor.execute(query_update,values)
            messagebox.showinfo("success","user updated successfully")
            editor.destroy()
            con.commit()
            con.close()
    except mysql.Error as err:
        messagebox.showerror('Database error',err)


button_logout=Button(root,text="logout",font=("Arial",16,"bold"),fg="blue",bg="#FFFACD",command=logout)
button_logout.place(x=1305,y=20)

# all the information of users are displayed when calling this function
# user information can be deleted and updated inside this function.
def frame_user():

    
    global username_entry
    def delete():
        global userName
        userName = None
        con = mysql.connect(host='localhost', user='root',
                        password="12345", port="3306", database='signup')
        cursor = con.cursor()
        username1 = username_entry.get()
        a='select username from user where username=%s'
        cursor.execute(a,(username1,))
        r=cursor.fetchone()
        if(r != None):
            userName = list(r)[0]
        if userName==username1:
            query1 = "delete from user where username =%s"
            cursor.execute(query1,(username1,))
            messagebox.showinfo("sucess","Deleted successfully")
        else:
            messagebox.showerror("error","Username not found")
        username_entry.delete(0,END) 
        con.commit()
        con.close()
    

    # user information are displayed for updation purpose
    def edit():
        global username1
        global editor
        global username_entry
        global name_entry
        global username_entry1
        global email_entry
        global address_entry
        global contact_no_entry
        global userName
        userName = None
        con = mysql.connect(host='localhost', user='root',
                        password="12345", port="3306", database='signup')
        cursor = con.cursor()
        username1 = username_entry.get()
        a='select username from user where username=%s'
        cursor.execute(a,(username1,))
        r=cursor.fetchone()
        if r != None:
            userName = list(r)[0]
        if userName==username1:
            editor =Tk()
            editor.title("update data")
            editor.geometry("300x400")
            editor.config(bg="#FFFACD")

            #this function runs after edit function to update the users data by entering data inside the entry boxes 
           
            def update():
                con = mysql.connect(host='localhost', user='root',
                                password="12345", port="3306", database='signup')
                cursor = con.cursor()
                a='select name,username,email,address,contact_no from user where username =%s'
                cursor.execute(a,(username1,))
                r=cursor.fetchone()
                b = list(r)
                if r != None:
                    name = b[0]
                    username = b[1]
                    email = b[2]
                    address = b[3]
                    contact_no =b[4]
                    name_entry.insert(0,name)
                    username_entry1.insert(0,username)
                    email_entry.insert(0,email)
                    address_entry.insert(0,address)
                    contact_no_entry.insert(0,contact_no)


            
            # create labels and entries  inside the editor window
            # editor window is for updating user's data 
            name = Label(editor,text = "Name",font=14,bg="#FFFACD",fg="#40E0D0")
            name.place(x=50,y=20)

            name_entry = Entry(editor)
            name_entry.place(x=140,y=20)

            username = Label(editor,text = "Username",font=14,bg="#FFFACD",fg="#40E0D0")
            username.place(x=50,y=100)

            username_entry1 = Entry(editor)
            username_entry1.place(x=140,y=100)

            email = Label(editor,text = "Email",font=14,bg="#FFFACD",fg="#40E0D0")
            email.place(x=50,y=180)

            email_entry = Entry(editor)
            email_entry.place(x=140,y=180)

            address = Label(editor,text = "Address",font=14,bg="#FFFACD",fg="#40E0D0")
            address.place(x=50,y=260)

            address_entry = Entry(editor)
            address_entry.place(x=140,y=260)

            contact_no = Label(editor,text = "Contact_No",font=14,bg="#FFFACD",fg="#40E0D0")
            contact_no.place(x=50,y=340)

            contact_no_entry = Entry(editor)
            contact_no_entry.place(x=140,y=340)
            
            save_btn = Button(editor,text ="Save",command=save,bg="#6495ED")
            save_btn.place(x=130,y=370)
        con.commit()
        con.close()
        update()

    
    frame_all.place(x=260,y=60)
    clear_frame()   # clears the previous frame to save the data inside  this frame
    


    # create frame for the labels in user information   
    frame = Frame(frame_all,width=1200,height=50,bg="light salmon") 
    frame.place(x=0,y=50)
    frame_all.config(bg="#FFFACD")

    name_label = Label(frame, text="Name",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    name_label.place(x=50, y=10) 

    username_label = Label(frame, text="Username",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    username_label.place(x=230, y=10)

    email_label = Label(frame, text="Email",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    email_label.place(x=430, y=10) 

    address_label = Label(frame, text="Address",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    address_label.place(x=600, y=10)

    contact_no_label = Label(frame, text="Contact No",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    contact_no_label.place(x=770, y=10) 

    password_label = Label(frame, text="Password",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    password_label.place(x=990, y=10) 


    # create frame for the user information fetched from database
    frame_user_data=Frame(frame_all,width=1140,height=800,bg="medium aquamarine")
    frame_user_data.place(x=0,y=100)
    con = mysql.connect(host='localhost', user='root',
                        password="12345", port="3306", database='signup')
    cursor = con.cursor()
    query1 = 'select * from user'
    cursor.execute(query1)
    row1 = cursor.fetchall()

    a = list(row1)
    c = 20
    d = 20
    e = 20
    f = 20
    g = 20
    h = 20
    for i in a:
        b = list(i)
        # create labels inside the frame_user_data fetched from the database
        Label(frame_user_data, text=b[0], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=40, y=c)
        c = c+40
        Label(frame_user_data, text=b[1], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=240, y=d)
        d = d+40
        Label(frame_user_data, text=b[2], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=400, y=e)
        e = e+40
        Label(frame_user_data, text=b[3], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=610, y=f)
        f = f+40       
        Label(frame_user_data, text=b[4], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=780, y=g)
        g = g+40
        Label(frame_user_data, text=b[5], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=990, y=h)
        h = h+40
    username_label=Label(frame_all,text="Username",font=16,bg="#FFFACD")
    username_label.place(x=290,y=0)
    username_entry= Entry(frame_all,width=28)
    username_entry.place(x=250,y=20,height=28)
    del_btn= Button(frame_all,text="Delete",command=delete,bg="#CD5C5C")
    del_btn.place(x=450,y=20)
    edit_btn = Button(frame_all,text="Edit",command=edit,bg="#FBBF00")
    edit_btn.place(x=550,y=20)
    con.commit()
    con.close()


# displays the username, problems and feedback sent by user
def frame_feedback():
    
    frame_all.place(x=260,y=50) # place the global frame
    frame_all.config(bg="#FFFACD")
    clear_frame()
    
    frame_label=Frame(frame_all,width=1200,bg="light salmon")
    frame_label.place(x=0,y=20,height=50)
    username_label=Label(frame_label,text="Username",fg ="blue",
            font=("poppins", 15),bg="light salmon")
    username_label.place(x=50,y=20)
    problems_label=Label(frame_label,text="Problems",fg ="blue",
            font=("poppins", 15),bg="light salmon")
    problems_label.place(x=350,y=20)
    feedback_label=Label(frame_label,text="Feedback",fg ="blue",
            font=("poppins", 15),bg="light salmon")
    feedback_label.place(x=750,y=20)
    frame_feedback=Frame(frame_all,width=1200,height=900,bg="medium aquamarine")
    frame_feedback.place(x=0,y=70)
           
    con = mysql.connect(host='localhost', user='root',
                        password="12345", port="3306", database='help')
    cursor = con.cursor()
    query1 = 'select * from feed'
    cursor.execute(query1)
    row1 = cursor.fetchall()
# all fetched data are stored in a row  according to the database
    a = list(row1)
    c =75
    d =75
    e =75
    for i in a:

        b = list(i)
        #set the data in labels from the database in a sequential order
        Label(frame_all, text=b[0], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=50, y=c)
        c = c+40
        Label(frame_all, text=b[1], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=350, y=d)
        d = d+40
        Label(frame_all, text=b[2], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=750, y=e)
        e = e+40
    con.commit()
    con.close()


# displays  the form details  filled by user while booking
def frame_formdetails():
    frame_all.place(x=260,y=70)
    clear_frame()
    frame_form_label=Frame(frame_all,width=1200,bg="light salmon")
    frame_form_label.place(x=0,y=0,height=55)
    frame_user=Frame(frame_all,width=1200,height=1000,bg="medium aquamarine")
    frame_user.place(x=0,y=50)

    name_label=Label(frame_form_label,text="Name",fg ="blue",
            font=("poppins", 13),bg="lightsalmon")
    name_label.place(x=30,y=12)
    name_label=Label(frame_form_label,text="Email",fg ="blue",
            font=("poppins", 13),bg="lightsalmon")
    name_label.place(x=160,y=12)
    name_label=Label(frame_form_label,text="Contact No",fg ="blue",
            font=("poppins", 13),bg="lightsalmon")
    name_label.place(x=320,y=12)
    name_label=Label(frame_form_label,text="Address",fg ="blue",
            font=("poppins", 13),bg="lightsalmon")
    name_label.place(x=455,y=12)
    name_label=Label(frame_form_label,text="Destination",fg ="blue",
            font=("poppins", 13),bg="lightsalmon")
    name_label.place(x=570,y=12)
    name_label=Label(frame_form_label,text="Visitors",fg ="blue",
            font=("poppins", 13),bg="lightsalmon")
    name_label.place(x=710,y=12)
    name_label=Label(frame_form_label,text="Tour Guides",fg ="blue",
            font=("poppins", 13),bg="lightsalmon")
    name_label.place(x=790,y=12)
    name_label=Label(frame_form_label,text="Start Date",fg ="blue",
            font=("poppins", 13),bg="lightsalmon")
    name_label.place(x=930,y=12)
    name_label=Label(frame_form_label,text="End Date",fg ="blue",
            font=("poppins", 13),bg="lightsalmon")
    name_label.place(x=1050,y=12)
    



    con = mysql.connect(host='localhost', user='root',
                        password="12345", port="3306", database='form')
    cursor = con.cursor()
    query1 = 'select * from details'
    cursor.execute(query1)
    row1 = cursor.fetchall()

    a = list(row1)
    c = 20
    d = 20
    e = 20
    f = 20
    g = 20
    h = 20
    j=20
    k=20
    l=20
    for i in a:
        b = list(i)
        Label(frame_user, text=b[0], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=0, y=c)
        c = c+40
        Label(frame_user, text=b[1], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=140, y=d)
        d = d+40
        Label(frame_user, text=b[2], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=320, y=e)
        e = e+40
        Label(frame_user, text=b[3], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=450, y=f)
        f = f+40       
        Label(frame_user, text=b[4], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=580, y=g)
        g = g+40
        Label(frame_user, text=b[5], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=730, y=h)
        h = h+40
        Label(frame_user, text=b[6], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=820, y=j)
        j = j+40
        Label(frame_user, text=b[7], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=930, y=k)
        k = k+40
        Label(frame_user, text=b[8], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=1050, y=l)
        l = l+40
    con.commit()
    con.close()

def clear_frame(): # define a function to clear frame
    for frame in frame_all.winfo_children(): 
        # clear all the children frame
        frame.destroy()


# create a options frame for placing buttons
options_frame=Frame(root,width=250,height=800,bg="#FFFACD")
options_frame.place(x=0,y=0)
label_options=Label(options_frame,text="Dashboard",font=("Arial",29,"bold"),fg="black",bg="#FFFACD")
label_options.place(x=0,y=0)
User_info_btn=Button(options_frame,text="User Information",font=("Arial",22,"bold"),fg="blue",bg="#FFFACD",command=frame_user,bd=0)
User_info_btn.place(x=0,y=120)
button_help_feedback=Button(options_frame,text="Help Requested",font=("Arial",22,"bold"),fg="blue",bg="#FFFACD",command=frame_feedback,bd=0)
button_help_feedback.place(x=0,y=230)
button_form_details=Button(options_frame,text="Form Details",font=("Arial",22,"bold"),fg="blue",bg="#FFFACD",command=frame_formdetails,bd=0)
button_form_details.place(x=0,y=340)

frame_all.place(x=260,y=60)  # place the global frame to insert picture inside this frame
image=Image.open("dash1.png")

image_resize=image.resize((1300,1300))
converted=ImageTk.PhotoImage(image_resize)
label=Label(frame_all,image=converted)
label.place(x=0,y=0)
root.mainloop()