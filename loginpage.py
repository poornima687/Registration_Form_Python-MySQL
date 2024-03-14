#for creating gui we have to import tkinter.. then we can call all classes,methods in tkinter
from tkinter import *
#importing python image library(PIL) for giving access to images
#for install that you have to install by typing in terminal "pip install pillow"
from PIL import ImageTk
from tkinter import messagebox
import pymysql as pms

#--------functions------------
def forgetPassword():
    #root.destroy()
    #import forgetPassword

    def changepassword():
        if usernameentry.get() == '' or passwordentry.get() == '' or confirmpasswordentry.get() == '':
            messagebox.showerror('Error', 'All feilds are required', parent=window)
        elif passwordentry.get() != confirmpasswordentry.get():
            messagebox.showerror('Error', 'Password and confirm password are not matched', parent=window)
        else:
            con = pms.connect(host='localhost', user='root', password='******', database='studentform')
            mycursor = con.cursor()
            query = 'select * from pstudent where username=%s'
            mycursor.execute(query, usernameentry.get())
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Incorrect username', parent=window)
            else:
                query = 'update pstudent set password=%s where username=%s'
                mycursor.execute(query, (passwordentry.get(), confirmpasswordentry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'changing password is successful', parent=window)
                window.destroy()


    # import forgetPassword
    #window = Tk()
    window=Toplevel()
    window.geometry('416x260+500+250')  # 200 means the x and y from the computer border
    window.title("Reset password")
    window.resizable(False, False)

    bgimage = ImageTk.PhotoImage(file='bg1.jpg')
    bglabel = Label(window, image=bgimage)
    bglabel.place(x=0, y=0)

    frame = Frame(window, width=350, height=235, bg='#ffff66')
    frame.place(x=45, y=15)

    heading = Label(window, text="Reset Password", font=('Comic Sans MS', 18, 'bold'), fg="brown", bg='#ffff66')
    heading.place(x=140, y=22)

    username = Label(window, text="Username", font=('Comic Sans MS', 11, 'bold'), bg='#ffff66', bd=0)
    username.place(x=70, y=75)
    usernameentry = Entry(window, width=27, font=('Comic Sans MS', 10), bg='white')
    usernameentry.place(x=160, y=75)

    password = Label(window, text="New Password", font=('Comic Sans MS', 11, 'bold'), bg='#ffff66', bd=0)
    password.place(x=70, y=100)
    passwordentry = Entry(window, width=23, font=('Comic Sans MS', 10), bg='white', show='*')
    passwordentry.place(x=190, y=100)

    confirmpassword = Label(window, text="Confirm Password", font=('Comic Sans MS', 11, 'bold'), bg='#ffff66', bd=0)
    confirmpassword.place(x=70, y=125)
    confirmpasswordentry = Entry(window, width=21, font=('Comic Sans MS', 10), bg='white', show='*')
    confirmpasswordentry.place(x=205, y=125)

    resetbtn = Button(window, text='Reset password', font=('Comic Sans MS', 13), command=changepassword, fg='white',
                      bg='brown',
                      activeforeground='black', activebackground='brown', bd=0, width=32, cursor='hand2')
    resetbtn.place(x=60, y=175)

    window.mainloop()


def onLogin():
    if (not usernameentry.get()) or (not passwordentry.get()):
        messagebox.showerror('Error',"Username or password is empty.")
    else:
        try:
            con=pms.connect(host='localhost',user='root',password='ganga687')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', "Database Connectivity Issue")
            return

        query = 'USE studentform'
        mycursor.execute(query)
        query = 'select * from pstudent where username=%s and password=%s'
        mycursor.execute(query,(usernameentry.get(),passwordentry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid details')
        else:
            messagebox.showinfo('Success','login is successful')

    root.destroy()

def moveToLogin():
    root.destroy()
    import signinpage

#------GUI--------
#create a object variable root and method called Tk
root=Tk()
root.geometry('416x260+500+250') #200 means the x and y from the computer border
root.title("LogIn")
root.resizable(False,False) # false foe height and width

#put image to backgroung image to window
bgimage=ImageTk.PhotoImage(file='bg1.jpg')

#creating the label for window
bglabel=Label(root,image=bgimage)
bglabel.place(x=0,y=0)  #when we use bglabel.place(x=0,y=0) this gives smal window not including full background image

#create a frame(yellow color background)
frame=Frame(root,width=350,height=235,bg='#ffff66')
frame.place(x=45,y=15)

#creating a heading for window
heading=Label(root,text="USER LOGIN",font=('Comic Sans MS',18,'bold'),fg="brown",bg='#ffff66')
heading.place(x=140,y=22)

#create username entry
username=Label(root,text="Username",font=('Comic Sans MS',11,'bold'),bg='#ffff66',bd=0)
username.place(x=75,y=70)
usernameentry=Entry(root,width=26,font=('Comic Sans MS',10),bg='white')
usernameentry.place(x=170,y=70)

#creating password entry
password=Label(root,text="Password",font=('Comic Sans MS',11,'bold'),bg='#ffff66')
password.place(x=75,y=110)
passwordentry=Entry(root,width=35,show="*",bg='white')
passwordentry.place(x=170,y=110)


#creating forget password section
forgetpassword=Button(root,text="Did you forget your password?",font=("Amasis MT Pro Black",10,'italic'),bd=0,activeforeground='blue',activebackground='#ffff66',cursor='hand2',bg='#ffff66',command=forgetPassword)
forgetpassword.place(x=200,y=135)

#Creating a button to submit
loginbtn=Button(root,text='Login',font=('Comic Sans MS',13),command=onLogin,fg='white',bg='brown',activeforeground='black',activebackground='brown',bd=0,width=32,cursor='hand2')
loginbtn.place(x=60,y=175)

#crreating a new account (moving to the sign in page)
noaccount=Label(root,text="Don't you have an account?",font=('Amasis MT Pro Black',10,'italic'),bg='#ffff66')
noaccount.place(x=70,y=220)
createnewbutton=Button(text='Create new account',command=moveToLogin,cursor='hand2',font=('Amasis MT Pro Black',9,'italic','bold','underline'),bg='#ffff66',fg='blue',activeforeground='brown',activebackground='#ffff66',bd=0)
createnewbutton.place(x=235,y=220)


#create a background
root.mainloop()