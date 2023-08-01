# importing all the necessary modules...
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mysql
# import bcrypt

# creating the tkinter window to setup widgets...
root = Tk()
# root.state("zoomed")
root.geometry("1500x900")
root.resizable(0,0)
root.title("Login Page")
root.config(bg = "#4785CF")

# function to clear up the entryfield on focus...
# def on_click_fName(e):
#     fNameSignupEntry.delete(0, END)

# def on_click_lName(e):
#     lNameSignupEntry.delete(0, END)

# def on_click_pwd(e):
#     pwdSignupEntry.delete(0, END)

# def on_click_cfmPwd(e):
#     cfmpwdSignupEntry.delete(0, END)



# calling the login function whenever user clicks on already have an account aka login...
def backLogin():
    root.destroy()
    import loginui



# calling the signup function whenver user clicks on don't have an account aka create one...
def backSignup():
    root.destroy()
    import finalsignin


# to check the user details, should have to use database fetching for user validation...
def loginFunc():
    email = UsernameEntry.get()
    password = pwdEntry.get()
    con = mysql.connect(host="localhost",user="root",password="12345",database="signup")
    cursor = con.cursor()
    a='SELECT  * FROM user WHERE username=%s and password=%s'
    cursor.execute(a,(email,password))
    r=cursor.fetchone()
    if r==None:
        messagebox.showerror("error","Invalid login")
    else:
        messagebox.showinfo("sucess","Logged in successfully")


# to have the user details, should have to use database to store user's data...
# def signupFunc():
#     messagebox.showinfo("Success", "Account successfully created")

# singup widget setup including labels and the entry fields and buttons...
# def signup():
#     global fNameSignupEntry, lNameSignupEntry, pwdSignupEntry, cfmpwdSignupEntry, entryImageSignupLabel

#     entryImageLoginLabel.destroy()
#     entryImageSignupLabel = Label(backgroundImageLabel, image = imageEntrySignup, border = 0, bg = "#4785CF")
#     entryImageSignupLabel.place(x = 96, y = 154)

#     createAccountText = Label(entryImageSignupLabel, text = "Create an account", font = ("Open Sans", 14, "bold"), bg = "#FFF", fg = "#000")
#     createAccountText.place(x = 112, y = 40)

#     loginIconLabel = Label(entryImageSignupLabel, image = iconLogin, bg = "#FFF")
#     loginIconLabel.place(x = 164, y = 84)

#     fNameSignupEntry = Entry(entryImageSignupLabel, width = 12, border = 0, bg = "#FFF", font = ("Tahoma", 12))
#     fNameSignupEntry.insert(0, "First Name")
#     fNameSignupEntry.bind("<FocusIn>", on_click_fName)
#     fNameSignupEntry.place(x = 66, y = 167, height = 30)

#     lNameSignupEntry = Entry(entryImageSignupLabel, width = 12, border = 0, bg = "#FFF", font = ("Tahoma", 12))
#     lNameSignupEntry.insert(0, "Last Name")
#     lNameSignupEntry.bind("<FocusIn>", on_click_lName)
#     lNameSignupEntry.place(x = 240, y = 167, height = 30)

#     pwdSignupEntry = Entry(entryImageSignupLabel, width = 32, border = 0, bg = "#FFF", font = ("Tahoma", 12))
#     pwdSignupEntry.insert(0, "New Password")
#     pwdSignupEntry.bind("<FocusIn>", on_click_pwd)
#     pwdSignupEntry.place(x = 64, y = 247, height = 30)

#     cfmpwdSignupEntry = Entry(entryImageSignupLabel, width = 32, border = 0, bg = "#FFF", font = ("Tahoma", 12))
#     cfmpwdSignupEntry.insert(0, "Confirm Password")
#     cfmpwdSignupEntry.bind("<FocusIn>", on_click_cfmPwd)
#     cfmpwdSignupEntry.place(x = 64, y = 326, height = 30)

#     loginButton = Button(entryImageSignupLabel, width = 136, image = imageButton, compound = CENTER, text = "CREATE", bg = "#FFF", border = 0, fg = "#000", command = signupFunc)
#     loginButton.place(x = 136, y = 376, height = 36)

#     signupText = Label(entryImageSignupLabel, text = "Already have an account?", bg = "#FFF", font = ("Tahoma", 10), fg = "#000")
#     signupText.place(x = 106, y = 432)

    # backLoginButton = Button(entryImageSignupLabel, text = "Login", fg = "blue", border = 0, bg = "#FFF", command = backLogin)
    # backLoginButton.place(x = 258, y = 433)


# all the images that have been used in creating login page...
imageBackground = Image.open("tourMainBg.png")
backgroundImage = ImageTk.PhotoImage(imageBackground)

loginIcon = Image.open("flight.png")
iconLogin = ImageTk.PhotoImage(loginIcon)

entryImageLogin = Image.open("entryImageLogin.png")
imageEntryLogin = ImageTk.PhotoImage(entryImageLogin)

entryImageSignup = Image.open("entryImageSignup.png")
imageEntrySignup = ImageTk.PhotoImage(entryImageSignup)

buttonImage = Image.open("button.png")
imageButton = ImageTk.PhotoImage(buttonImage)

backgroundImageLabel = Label(root, image = backgroundImage, border = 0)
backgroundImageLabel.place(x = 92, y = 34)



# setting up widgets for login page including labels, entryfields and buttons as well...
def login():

    global entryImageLoginLabel, UsernameEntry, pwdEntry

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


# calling login function here means that login page will be our default opening...
login()

root.mainloop()