# importing all the necessary modules...
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mysql
# import bcrypt

# creating the tkinter window to setup widgets...
root = Tk()

root.geometry("1500x900")
root.resizable(0,0)
root.title("Login Page")
root.config(bg = "#4785CF")

# calling the signup function whenver user clicks on don't have an account aka create one...
def backSignup():
    root.destroy()
    import finalsignin

# to check the user details, using database fetching for user validation...
def loginFunc():
    
    email = UsernameEntry.get()
    password = pwdEntry.get()
    if email=="krishna" and password=="12345":
        root.destroy()
        import admin
    else:
        try:
            con = mysql.connect(host="localhost",user="root",password="12345",database="signup")
            cursor = con.cursor()
            a='SELECT  * FROM user WHERE username=%s and password=%s'
            cursor.execute(a,(email,password))
            r=cursor.fetchone()
            if r==None:
                messagebox.showerror("error","Invalid login")
            else:
                messagebox.showinfo("sucess","Logged in successfully")
                root.destroy()
                import Tour
            con.commit()
            con.close()
        except Exception as err:
            messagebox.showerror("Error","An error occured")
# all the images that have been used in creating login page...
imageBackground = Image.open("tourMainBg.png")
backgroundImage = ImageTk.PhotoImage(imageBackground)

loginIcon = Image.open("flight.png")
iconLogin = ImageTk.PhotoImage(loginIcon)

entryImageLogin = Image.open("entryImageLogin.png")
imageEntryLogin = ImageTk.PhotoImage(entryImageLogin)


buttonImage = Image.open("button.png")
imageButton = ImageTk.PhotoImage(buttonImage)

backgroundImageLabel = Label(root, image = backgroundImage, border = 0)
backgroundImageLabel.place(x = 92, y = 34)

# setting up widgets for login page including labels, entryfields and buttons as well...

entryImageLoginLabel = Label(backgroundImageLabel, image = imageEntryLogin, border = 0, bg = "#4785CF")
entryImageLoginLabel.place(x = 96, y = 154)

headingTitle = Label(text = "TOURS AND TRAVELS PVT LTD.", font = ("Yu Gothic Semibold", 18, "bold"), bg = "#4785CF", fg = "#FFF")
headingTitle.place(x = 212, y = 78)

welcomeText = Label(entryImageLoginLabel, text = "Welcome! Login Here", font = ("Open Sans", 14, "bold"), bg = "#FFF", fg = "#000")
welcomeText.place(x = 102, y = 40)

loginIconLabel = Label(entryImageLoginLabel, image = iconLogin, bg = "#FFF")
loginIconLabel.place(x = 164, y = 84)

UsernameLabel = Label(entryImageLoginLabel, text = "Username •", bg = "#FFF", font = ("Tahoma", 12), fg = "#000")
UsernameLabel.place(x = 68, y = 156)

UsernameEntry = Entry(entryImageLoginLabel, width = 30, border = 0, bg = "#FFF", font = ("Tahoma", 12))
UsernameEntry.place(x = 68, y = 188, height = 30)

pwdLabel = Label(entryImageLoginLabel, text = "Password •", bg = "#FFF", font = ("Tahoma", 12), fg = "#000")
pwdLabel.place(x = 70, y = 254)

pwdEntry = Entry(entryImageLoginLabel, width = 30, border = 0, bg = "#FFF", font = ("Tahoma", 12))
pwdEntry.place(x = 70, y = 288, height = 30)

loginButton = Button(entryImageLoginLabel, width = 136, image = imageButton, compound = CENTER, text = "LOGIN", bg = "#FFF", border = 0, fg = "#000", cursor = "hand2", command = loginFunc)
loginButton.place(x = 136, y = 356, height = 36)

signupText = Label(entryImageLoginLabel, text = "Don't have an account?", bg = "#FFF", font = ("Tahoma", 10), fg = "#000")
signupText.place(x = 100, y = 432)

createButton = Button(entryImageLoginLabel, text = "Create one", fg = "blue", border = 0, bg = "#FFF", cursor = "hand2", command = backSignup)
createButton.place(x = 236, y = 433)

root.mainloop()