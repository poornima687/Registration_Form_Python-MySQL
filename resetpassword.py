from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql as pms


def changepassword():
    if usernameentry.get() == '' or passwordentry.get() == '' or confirmpasswordentry.get() == '':
        messagebox.showerror('Error', 'All feilds are required', parent=window)
    elif passwordentry.get() != confirmpasswordentry.get():
        messagebox.showerror('Error', 'Password and confirm password are not matched', parent=window)
    else:
        con = pms.connect(host='localhost', user='window', password='*****', database='studentform')
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
            import loginpage


# import forgetPassword
window = Tk()
#window=Toplevel()
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

resetbtn = Button( window,text='Reset password', font=('Comic Sans MS', 13), command=changepassword, fg='white',
                  bg='brown',
                  activeforeground='black', activebackground='brown', bd=0, width=32, cursor='hand2')
resetbtn.place(x=60, y=175)

window.mainloop()