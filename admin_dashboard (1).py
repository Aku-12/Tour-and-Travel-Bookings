from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox
root=Tk()
root.geometry("1400x1400")
root.resizable(0,0)
root.title("Admin Panel")
label_roots=Label(root,text="Travel and Tour Booking System",font=("arial",29,"bold"),fg="orange")
label_roots.pack()


def logout():   
    import loginui
    root.destroy()

def save():
    name =name_entry.get()
    email =email_entry.get()
    address =address_entry.get()
    contact_no =contact_no_entry.get()
    if name_entry.get()=="" or username_entry1.get()=="" or email_entry.get()=="" or address_entry.get()=="" or contact_no_entry.get()=="":
        messagebox.showerror("error","All fields are required")
    else:
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


button_logout=Button(root,text="logout",font=("Arial",22,"bold"),fg="blue",bg="#FFFACD",command=logout)
button_logout.place(x=905,y=0)

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
            editor.geometry("1000x1000")
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

            name = Label(editor,text = "name")
            name.place(x=50,y=20)

            name_entry = Entry(editor)
            name_entry.place(x=110,y=20)

            username = Label(editor,text = "username")
            username.place(x=50,y=100)

            username_entry1 = Entry(editor)
            username_entry1.place(x=110,y=100)

            email = Label(editor,text = "email")
            email.place(x=50,y=180)

            email_entry = Entry(editor)
            email_entry.place(x=110,y=180)

            address = Label(editor,text = "address")
            address.place(x=50,y=240)

            address_entry = Entry(editor)
            address_entry.place(x=110,y=240)

            contact_no = Label(editor,text = "contact_no")
            contact_no.place(x=50,y=320)

            contact_no_entry = Entry(editor)
            contact_no_entry.place(x=110,y=320)
            
            save_btn = Button(editor,text ="save",command=save)
            save_btn.place(x=80,y=450)
        con.commit()
        con.close()
        update()
                
    frame = Frame(root,width=630,height=100,bg="light salmon") 
    frame.place(x=200,y=100)

    name_label = Label(frame, text="Name",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    name_label.place(x=30, y=30) 

    username_label = Label(frame, text="Username",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    username_label.place(x=120, y=30)

    email_label = Label(frame, text="Email",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    email_label.place(x=235, y=30) 

    address_label = Label(frame, text="Address",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    address_label.place(x=330, y=30)

    contact_no_label = Label(frame, text="Contact No",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    contact_no_label.place(x=420, y=30) 

    password_label = Label(frame, text="Password",bg ="light salmon",fg ="blue",
            font=("poppins", 15))
    password_label.place(x=530, y=30) 

    frame_user=Frame(root,width=630,height=800,bg="medium aquamarine")
    frame_user.place(x=200,y=190)
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
        Label(frame_user, text=b[0], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=40, y=c)
        c = c+40
        Label(frame_user, text=b[1], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=140, y=d)
        d = d+40
        Label(frame_user, text=b[2], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=240, y=e)
        e = e+40
        Label(frame_user, text=b[3], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=340, y=f)
        f = f+40       
        Label(frame_user, text=b[4], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=440, y=g)
        g = g+40
        Label(frame_user, text=b[5], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=540, y=h)
        h = h+40
    username_entry= Entry(root)
    username_entry.place(x=250,y=50)
    del_btn= Button(root,text="Delete",command=delete)
    del_btn.place(x=400,y=50)
    edit_btn = Button(root,text="Edit",command=edit)
    edit_btn.place(x=500,y=50)
    con.commit()
    con.close()


def frame_feedback():
    frame_feedback=Frame(root,width=800,height=800,bg="#FFFACD")
    frame_feedback.place(x=200,y=50)
    con = mysql.connect(host='localhost', user='root',
                        password="12345", port="3306", database='help')
    cursor = con.cursor()
    query1 = 'select * from feed'
    cursor.execute(query1)
    row1 = cursor.fetchall()
    a = list(row1)
    c = 20
    d = 20
    e = 20
    for i in a:
        b = list(i)
        Label(frame_feedback, text=b[0], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=40, y=c)
        c = c+40
        Label(frame_feedback, text=b[1], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=140, y=d)
        d = d+40
        Label(frame_feedback, text=b[2], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=240, y=e)
        e = e+40
    con.commit()
    con.close()


def frame_formdetails():

    frame_user=Frame(root,width=1200,height=1000,bg="#FFFACD")
    frame_user.place(x=200,y=190)
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
            font=("poppins", 12)).place(x=40, y=c)
        c = c+40
        Label(frame_user, text=b[1], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=140, y=d)
        d = d+40
        Label(frame_user, text=b[2], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=240, y=e)
        e = e+40
        Label(frame_user, text=b[3], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=340, y=f)
        f = f+40       
        Label(frame_user, text=b[4], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=440, y=g)
        g = g+40
        Label(frame_user, text=b[5], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=540, y=h)
        h = h+40
        Label(frame_user, text=b[6], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=640, y=j)
        j = j+40
        Label(frame_user, text=b[7], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=740, y=k)
        k = k+40
        Label(frame_user, text=b[8], bg='medium aquamarine',fg ="navy",
            font=("poppins", 12)).place(x=900, y=l)
        l = l+40
    con.commit()
    con.close()

options_frame=Frame(root,width=250,height=800,bg="#FFFACD")
options_frame.place(x=0,y=0)
label_options=Label(options_frame,text="Dashboard",font=("Arial",29,"bold"),fg="blue",bg="#FFFACD")
label_options.place(x=0,y=0)
User_info_btn=Button(options_frame,text="User Information",font=("Arial",22,"bold"),fg="blue",bg="#FFFACD",command=frame_user)
User_info_btn.place(x=0,y=50)
button_help_feedback=Button(options_frame,text="Help Requested",font=("Arial",22,"bold"),fg="blue",command=frame_feedback)
button_help_feedback.place(x=0,y=150)
button_form_details=Button(options_frame,text="Form Details",font=("Arial",22,"bold"),fg="blue",command=frame_formdetails)
button_form_details.place(x=0,y=250)
root.mainloop()