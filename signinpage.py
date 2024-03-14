from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
#installing pymysql type pip install pymysql on terminal
import pymysql as pms

def clear():
    usernameentry.delete(0,END)
    emailentry.delete(0,END)
    passwordentry.delete(0,END)
    confirmpasswordentry.delete(0,END)
    check.set(0)

def connectDatabase():
    if (not usernameentry.get() or (not emailentry.get()) or (not passwordentry.get()) or (not confirmpasswordentry.get())):
        messagebox.showerror('Error',"All details are required.")
    elif passwordentry.get() != confirmpasswordentry.get():
        messagebox.showerror('Error','password mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept rules and regulations')
    else:
        try:
            con=pms.connect(host='localhost',user='root',password='******')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error',"Database Connectivity Issue")
            return

        try:
            query='CREATE DATABASE studentform'
            mycursor.execute(query)
            query= 'USE studentform'
            mycursor.execute(query)
            query= 'CREATE TABLE PSTUDENT(ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,USERNAME VARCHAR(100),EMAIL VARCHAR(50),PASSWORD VARCHAR(50))'
            mycursor.execute(query)
            #con.commit()
        except:
            mycursor.execute('USE studentform')

        #check username whether already exists or not
        query='select * from pstudent where username=%s'
        mycursor.execute(query,(usernameentry.get()))

        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error','Username already exists')
        else:  #usernames are not same then we can insert data
            #con = pms.connect(host='localhost', user='root', password='ganga687',database='studentform')
            #mycursor = con.cursor()
            query='INSERT INTO pstudent(username,email,password) values(%s,%s,%s)'
            mycursor.execute(query,(usernameentry.get(),emailentry.get(),passwordentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('success','Registration is successful')
            clear()
            root.destroy()
            import loginpage


def moveToLoginpage():
    root.destroy()
    import loginpage

root=Tk()
root.geometry('416x260+500+250')
root.title("SignIn")
root.resizable(False,False) # false foe height and width

sbgimage=ImageTk.PhotoImage(file='bg1.jpg')
sbglabel=Label(root,image=sbgimage)
sbglabel.place(x=0,y=0)

frame=Frame(root,width=350,height=240,bg='#ffff66')
frame.place(x=45,y=10)

heading=Label(root,text='USER SIGN IN',font=('Comic Sans MS',16,"bold"),fg='brown',bg='#ffff66')
heading.place(x=140,y=10)

username=Label(root,text="Username",font=('Comic Sans MS',11,'bold'),bg='#ffff66',bd=0)
username.place(x=70,y=50)
usernameentry=Entry(root,width=27,font=('Comic Sans MS',10),bg='white')
usernameentry.place(x=160,y=50)

email=Label(root,text="E-mail ",font=('Comic Sans MS',11,'bold'),bg='#ffff66',bd=0)
email.place(x=70,y=75)
emailentry=Entry(root,width=27,font=('Comic Sans MS',10),bg='white')
emailentry.place(x=160,y=75)

password=Label(root,text="Password",font=('Comic Sans MS',11,'bold'),bg='#ffff66',bd=0)
password.place(x=70,y=100)
passwordentry=Entry(root,width=27,font=('Comic Sans MS',10),bg='white',show='*')
passwordentry.place(x=160,y=100)

confirmpassword=Label(root,text="Confirm Password",font=('Comic Sans MS',11,'bold'),bg='#ffff66',bd=0)
confirmpassword.place(x=70,y=125)
confirmpasswordentry=Entry(root,width=21,font=('Comic Sans MS',10),bg='white',show='*')
confirmpasswordentry.place(x=205,y=125)

check=IntVar()
agreeCondition=Checkbutton(root,text='I agree to all rules and regulations',font=('Amasis MT Pro Black',9,'italic','bold'),fg='blue',bg='#ffff66',cursor='hand2',activeforeground='brown',activebackground='#ffff66',bd=0,variable=check)
agreeCondition.place(x=160,y=160)

signinbtn=Button(text="Signin",font=('Comic Sans MS',11,'bold'),fg='white',bg='brown',activeforeground='black',activebackground='brown',bd=0,width=33,cursor='hand2',command=connectDatabase)
signinbtn.place(x=70,y=185)

loginbutton=Button(text='Go to Login form',font=('Amasis MT Pro Black',9,'italic','bold','underline'),fg='blue',bg='#ffff66',cursor='hand2',activeforeground='brown',activebackground='#ffff66',bd=0,command=moveToLoginpage)
loginbutton.place(x=270,y=225)

root.mainloop()