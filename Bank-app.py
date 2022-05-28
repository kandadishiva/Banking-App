from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from captcha.image import ImageCaptcha
from datetime import datetime
import random
import re
import time
import fileinput
app=Tk()
app.title("Bank App")
app.geometry('325x580')
app.minsize(325,580)
app.maxsize(325, 580)

app.configure(bg="mint cream")

name=Label(app,text="   Infinity Bank",font="Times 20 italic bold",bg="mint cream")
name.grid(row=0,column=0,columnspan=3)

img=Image.open("infinity.ico")
re_img=img.resize((320,205), Image.ANTIALIAS)
img1=ImageTk.PhotoImage(re_img)
label1=Label(image=img1,fg="mint cream")
label1.grid(row=1,column=0,columnspan=3)


def forgot():
    return

def login1(w=0):
    if(w==0):
        app.destroy()
    login=Tk()
    login.title("Login")
    login.geometry("350x580")
    login.minsize(350,580)
    login.maxsize(350,580)
    login.configure(bg="mint cream")

    label_heading=Label(login,text=" Welcome to Ifinity Bank",bg="mint cream",font=("Comic Sans MS", 18, "bold"),pady=10,padx=10)
    label_heading.grid(row=0,column=0,columnspan=3)

    label_login = Label(login, text="Enter the login detailes", bg="mint cream", font="Times 15 italic bold", pady=10)
    label_username=Label(login,text="User Name : ",bg="mint cream",font ="Times 15 italic bold",pady=10)
    label_password = Label(login, text="Password : ", bg="mint cream", font="Times 15 italic bold", pady=10)
    label_captcha=Label(login,text="Captcha : ", bg="mint cream", font="Times 15 italic bold", pady=10)

    button_forgotPassword=Button(login,text="Forgot Password",command=forgot,bg="mint cream",font=("Century Schoolbook", 7, "bold"))
    button_forgotPassword.grid(row=6, column=1)


    label_empty2 = Label(login, bg="mint cream")
    label_empty2.grid(row=1, column=1, pady=8)

    label_empty3 = Label(login, bg="mint cream")
    label_empty3.grid(row=3, column=1, pady=8)

    label_empty4 = Label(login, bg="mint cream")
    label_empty4.grid(row=8, column=1, pady=3)

    label_login.grid(row=2,column=0,columnspan=2)
    label_username.grid(row=4, column=0)
    label_password.grid(row=5, column=0)
    label_captcha.grid(row=7,column=0)


    username=Entry(login,width=28)
    Password = Entry(login, width=28,show="*")
    Ecaptcha=Entry(login,width=28)

    username.grid(row=4,column=1)
    Password.grid(row=5,column=1)
    Ecaptcha.grid(row=8,column=1)


    def captchaF(c):
        q=c
        global button_captcha,captcha
        text='QWERTYUIOPASDFGHJKLZXCVBNM0123456789'
        captcha_text = random.choices(text, k=5)
        captcha = "".join(captcha_text)
        color=["Silver","Aqua","tomato","orange","coral","light steel blue"]
        fonts=["Century Schoolbook","Consolas","Arial Black","Cambria"]
        c=random.choice(color)
        f=random.choice(fonts)

        if(q==1):
            button_captcha.grid_forget()
            button_captcha = Button(login, text=captcha, command=lambda :captchaF(1), bg=c, font=(f, 15, "bold"))
            button_captcha.grid(row=7, column=1, columnspan=2)
        elif(q==0):
            button_captcha = Button(login, text=captcha, command=lambda : captchaF(1), bg=c,font=(f, 15, "bold"))
            button_captcha.grid(row=7, column=1, columnspan=2)

    captchaF(0)


    def loginC():
        global captcha,u
        u=username.get()
        p=Password.get()
        c=Ecaptcha.get()

        ca=captcha

        if(ca!=c):
            messagebox.showerror("Warning", "Enter Correct Captcha")
        elif(u[0:2]=="96"):
            f1=open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-savings-detailes.txt","r")
            l=0
            f=0
            fP=0
            for line in f1:
                l+=1
                ans=line
                lin=ans.split(" ")
                if u in lin:
                    f=1
                elif f==1:
                    if p in lin:
                        fP=1
                    break
            f1.close()
            if(f==1 and fP==1):
                login.destroy()
                home()
            elif(f==1 and fP==0):
                messagebox.showerror("Warning", "Enter Correct Password")
            else:
                messagebox.showerror("Warning", "Enter Correct User Name")
        elif (u[0:2] == "97"):
            f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-Current-detailes.txt","r")
            l = 0
            f = 0
            fP = 0
            for line in f1 :
                l += 1
                lin=line.split(" ")
                if u in lin:
                    f = 1
                elif f == 1:
                    if p in lin:
                        fP = 1
                    break
            f1.close()
            if (f == 1 and fP == 1):
                login.destroy()
                home()
            elif (f == 1 and fP == 0):
                messagebox.showerror("Warning", "Enter Correct Password")
            else:
                messagebox.showerror("Warning", "Enter Correct User Name")
        else:
            messagebox.showerror("Warning", "Enter Correct User Name")
        return

    button_Login1=Button(login,text="Login",command=loginC, bg="tan", fg="royal blue",font=("Century Schoolbook", 15, "bold"))
    button_Login1.grid(row=9,column=0,columnspan=2)

    return

#def confirm1():
#    global signup,Fname, Mname, Lname, Dob,Pfname,Pmname,Nname,Address,adhar,pan,phno
#
 #   a=phno.get()
  #  if(len(a)!=10):
#     label_worng=Label(signup,text="enter correct ph no")
 #       label_worng.grid(row=12,column=0,columnspan=2)
  #  return

def home():
    Home=Tk()
    Home.title("Home")
    Home.geometry("350x580")
    Home.minsize(350,580)
    Home.maxsize(350,580)
    Home.configure(bg="mint cream")

    global u

    label_home=Label(Home,text="   Home Page",bg="mint cream" ,font=("Comic Sans MS", 18, "bold"),pady=10)
    label_home.grid(row=0,column=0,columnspan=3)

    def logout():
        Home.destroy()
        log=Tk()
        log.title("Home")
        log.geometry("350x580")
        log.minsize(350, 580)
        log.maxsize(350, 580)
        log.configure(bg="mint cream")

        def Alogin():
            log.destroy()
            login1(1)

        label_empty8 = Label(log, bg="mint cream")
        label_empty8.grid(row=0, column=1, pady=10)

        label_logout=Label(log,text="You Have Been Successfully Logged Out",bg="mint cream",font=("Comic Sans MS", 13, "bold"))
        label_logout.grid(row=1,column=0)

        button_Login1=Button(log,text="Login",command=Alogin,font=("Comic Sans MS", 13, "bold"), bg="tan", fg="royal blue")
        button_Login1.grid(row=2,column=0,columnspan=3)

    button_logout=Button(Home,text="Logout",command=logout,bg="mint cream" ,font=("Comic Sans MS", 13, "bold"))
    button_logout.grid(row=1,column=2)

    f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customer-detailes.txt","r")
    c=0
    for line in f1:
        ans=line.split(" ")
        if (u in ans) and c==0:
            c=1
        if ("FullName" in ans) and c==1:
            Name1=ans[2]
            break;
    label_Name=Label(Home,text="Hlo "+ str(ans[2])+" "+str(ans[3])+" "+str(ans[4]),bg="mint cream",font=("Arial Black", 13, "bold"),pady=10)
    label_Name.grid(row=1,column=0,columnspan=2)

    label_empty3 = Label(Home, bg="mint cream")
    label_empty3.grid(row=2, column=1, pady=8)

    label_empty4 = Label(Home, bg="mint cream")
    label_empty4.grid(row=4, column=1, pady=8)

    label_empty5 = Label(Home, bg="mint cream")
    label_empty5.grid(row=7, column=1, pady=70)

    def Balance():
        global u
        if (u[0:2] == "96"):
            f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-savings-detailes.txt","r")
        elif (u[0:2] == "97"):
            f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-Current-detailes.txt","r")
        c=0
        for line in f1 :
            ans=line.split(" ")
            if (u in ans) and c==0:
                c=1
            if ("Account" in ans) and c==1:
                break;
        button_balance.grid_forget()
        label_balance=Label(Home,text=str(ans[3]),bg="mint cream",font ="Times 12 italic bold",pady=10,padx=10)
        label_balance.grid(row=3,column=0,columnspan=3)

    def send():
        Home.destroy()
        Send=Tk()
        Send.title("Payments")
        Send.geometry("350x580")
        Send.minsize(350, 580)
        Send.maxsize(350, 580)
        Send.configure(bg="mint cream")

        label_empty5 = Label(Send, bg="mint cream")
        label_empty5.grid(row=1, column=0, pady=30)


        label_text=Label(Send,text="Infinity Bank Payments",bg="mint cream",font =("Comic Sans MS", 18, "bold"),pady=10,padx=10)
        label_acc=Label(Send,text="Enter the Account number :",bg="mint cream",font ="Times 12 italic bold",pady=10)
        label_Smoney=Label(Send,text="Enter the money : ",bg="mint cream",font ="Times 12 italic bold",pady=10)

        label_text.grid(row=0, column=1, columnspan=2)
        label_acc.grid(row=2,column=0, columnspan=2)
        label_Smoney.grid(row=4,column=0,columnspan=2)

        entery_acc=Entry(Send,width=35)
        entery_Smoney=Entry(Send,width=35)

        entery_acc.grid(row=3,column=1)
        entery_Smoney.grid(row=5,column=1,pady=10)

        def transfer():
            global u

            s=entery_acc.get()
            m=entery_Smoney.get()
            if(s[0:2]=="96") :
                f1 = "\\Users\\91984\\Documents\\KLH UNIVERSITY\\PYTHON PROGRAMING\\Files\\Infinity Bank-Customers-savings-detailes.txt"
            elif (s[0:2] == "97"):
                f1 = "\\Users\\91984\\Documents\\KLH UNIVERSITY\\PYTHON PROGRAMING\\Files\\Infinity Bank-Customers-Current-detailes.txt"
            else:
                messagebox.showerror("Warning","Enter Correct User Name")
            f2=open(f1,"r")
            c=0
            com=0
            x=0
            line1=""
            for line in f2:
                an=line.split(" ")
                if s in an:
                    c=1
                    break
            f2.close()
            if c==1:
                if (u[0:2] == "96"):
                    f3 = "\\Users\\91984\\Documents\\KLH UNIVERSITY\\PYTHON PROGRAMING\\Files\\Infinity Bank-Customers-savings-detailes.txt"
                elif (u[0:2] == "97"):
                    f3 = "\\Users\\91984\\Documents\\KLH UNIVERSITY\\PYTHON PROGRAMING\\Files\\Infinity Bank-Customers-Current-detailes.txt"

                f2=open(f3,"r")
                c=0
                for line in f2:
                    an=line.split(" ")
                    if u in an and c==0:
                        c=1
                    if "Account" in an and c==1 and x==0:
                        res=int(an[3])
                        if res>=int(m):
                            res1 = res - int(m)
                            an.insert(3, str(res1))
                            an.remove(an[4])
                            line = " ".join(an)

                            ans = datetime.today().strftime("%d-%m-%Y")
                            sol = ans + " " + "-" + str(m) + " " + str(res1) + " " + "\n"
                            line = line + sol
                            com=40
                        else:
                            messagebox.showerror("Warning","insufficient Money")
                            break
                        x=1
                    line1=line1+line
                f2.close()
                if(com==40) :
                    f2=open(f3,"w")
                    f2.write((line1))
                    f2.close()
                    f2=open(f1,"r")
                    c=0
                    x=0
                    line1=""
                    for line in f2:
                        ans = line.split(" ")
                        if s in line and c == 0:
                            c = 1
                        if "Account" in line and c == 1 and x == 0:
                            res = int(ans[3]) + int(m)
                            ans.insert(3, str(res))
                            ans.remove(ans[4])
                            line = " ".join(ans)

                            ans = datetime.today().strftime("%d-%m-%Y")
                            sol = ans + " " + "+" + str(m) + " " + str(res) + " " + "\n"
                            line = line + sol
                            x=1
                        line1=line1+line
                    f2.close()
                    f2=open(f1,"w")
                    f2.write(line1)
                    f2.close()
                    messagebox.showinfo("Success","Success")
            else:
                messagebox.showerror("Warning", "Enter Correct User Name there is no such Account")

        button_Send1=Button(Send,text="Send",command=transfer,font=("Comic Sans MS", 13, "bold"), bg="tan", fg="royal blue",padx=10)
        button_Send1.grid(row=6,column=0,columnspan=3)

        def back():
            Send.destroy()
            home()

        button_back=Button(Send,text="<<",command=back,font=("Comic Sans MS", 13, "bold"), bg="tan", fg="royal blue")
        button_back.grid(row=0,column=0)

    def deposit():
        Home.destroy()
        Add = Tk()
        Add.title("Payments")
        Add.geometry("350x580")
        Add.minsize(350, 580)
        Add.maxsize(350, 580)
        Add.configure(bg="mint cream")

        global u

        label_empty5 = Label(Add, bg="mint cream")
        label_empty5.grid(row=1, column=0, pady=50)

        label_text = Label(Add, text="Infinity Bank Payments", bg="mint cream", font=("Comic Sans MS", 18, "bold"),pady=10, padx=10)
        label_enter = Label(Add, text="Enter the Money :", bg="mint cream", font="Times 12 italic bold",pady=10)

        label_text.grid(row=0, column=1, columnspan=2)
        label_enter.grid(row=2, column=0, columnspan=2)

        entery_Smoney = Entry(Add, width=35)
        entery_Smoney.grid(row=3, column=1, pady=10)

        def add():
            global u
            if (u[0:2] == "96"):
                f1 ="\\Users\\91984\\Documents\\KLH UNIVERSITY\\PYTHON PROGRAMING\\Files\\Infinity Bank-Customers-savings-detailes.txt"
            elif (u[0:2] == "97"):
                f1 ="\\Users\\91984\\Documents\\KLH UNIVERSITY\\PYTHON PROGRAMING\\Files\\Infinity Bank-Customers-Current-detailes.txt"
            line1=""
            c=0
            z=0
            x=0
            f2=open(f1,"r")
            for line in f2:
                ans = line.split(" ")
                if u in line and c==0:
                    c=1
                if "Account" in line and c==1 and x==0:
                    res=int(ans[3])+int(entery_Smoney.get())
                    ans.insert(3,str(res))
                    ans.remove(ans[4])
                    line=" ".join(ans)
                    x=1
                    z=1
                if z==1:
                    ans = datetime.today().strftime("%d-%m-%Y")
                    sol=ans+" "+"+"+entery_Smoney.get()+" "+str(res)+" "+"\n"
                    line=line+sol
                    z=0
                line1=line1+line
            f2.close()
            f2=open(f1,"w")
            f2.write(line1)
            f2.close()
            messagebox.showinfo("Success","Success")


        button_add=Button(Add,text="Add",command=add,font=("Comic Sans MS", 13, "bold"), bg="tan", fg="royal blue")
        button_add.grid(row=4,column=1)

        def back():
            Add.destroy()
            home()

        button_back=Button(Add,text="<<",command=back,font=("Comic Sans MS", 13, "bold"), bg="tan", fg="royal blue")
        button_back.grid(row=0,column=0)


    def statement():
        Home.destroy()
        state = Tk()
        state.title("Payments")
        state.geometry("350x580")
        state.minsize(350, 580)
        state.maxsize(350, 580)
        state.configure(bg="mint cream")

        global u

        label_text=Label(state,text="Mini Statement",bg="mint cream",font =("Comic Sans MS", 13, "bold"),pady=10,padx=10)
        label_text.grid(row=1,column=1,columnspan=2)

        label_headings=Label(state,text="Date Transfer balance",bg="mint cream",font ="Times 15 italic bold",pady=15)
        label_headings.grid(row=2,column=1,columnspan=2)

        if (u[0:2]=="96"):
            f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-savings-detailes.txt","r")
        else:
            f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-Current-detailes.txt","r")

        c=0
        co=1
        x=0
        z=0
        line1=""
        for line in f1:
            ans=line.split(" ")
            if u in ans and c==0:
                c=1
            if "Account" in ans and c==1 and x==0 and z==0:
                line=""
                x=1
                z=1
            if "Stop" in ans and x==1:
                break
            if x==1 and co<5 :
                line1=line1+line
                co=co+1

        label_statement=Label(state,text=line1,bg="mint cream",font ="Times 15 italic bold")
        label_statement.grid(row=3,column=1,columnspan=2)
        def back1():
            state.destroy()
            home()

        button_back = Button(state, text="<<", command=back1, font=("Comic Sans MS", 13, "bold"), bg="tan",fg="royal blue")
        button_back.grid(row=0, column=0)

    button_balance=Button(Home,text="View Balance",command=Balance,bg="mint cream",font ="Times 12 italic bold",pady=10,padx=10)
    button_Send = Button(Home, text="Send Money",command=send, bg="mint cream", font="Times 12 italic bold", pady=18,padx=5)
    button_Addmoney = Button(Home, text="Add Money",command=deposit, bg="mint cream", font="Times 12 italic bold", pady=18,padx=13)
    button_MRecharge = Button(Home, text="Mobile Recharge", bg="mint cream", font="Times 12 italic bold", pady=18,padx=0)
    button_Paybills = Button(Home, text="Pay Bills", bg="mint cream", font="Times 12 italic bold", pady=18,padx=12)
    button_Statement = Button(Home, text="View Statement", command=statement,bg="mint cream", font="Times 12 italic bold", pady=18,padx=0)


    button_balance.grid(row=3,column=0,columnspan=3)
    button_Send.grid(row=5,column=0)
    button_Addmoney.grid(row=5, column=1)
    button_MRecharge.grid(row=5, column=2)
    button_Paybills.grid(row=6, column=0)
    button_Statement.grid(row=6, column=1)

    def home1():
        Home.destroy()
        home()
    button_home=Button(Home,text="Home",bg="mint cream",command=home1,font ="Times 12 italic bold",pady=10,padx=20)
    button_support = Button(Home, text="Support(24/7)", bg="mint cream", font="Times 12 italic bold", pady=10, padx=10)
    button_settings= Button(Home, text="Settings", bg="mint cream", font="Times 12 italic bold", pady=10, padx=20)


    button_home.grid(row=8,column=0)
    button_support.grid(row=8, column=1)
    button_settings.grid(row=8, column=2)


def Opening_Ammount():
    opening=Tk()
    opening.geometry("350x580")
    opening.minsize(350,580)
    opening.maxsize(350,580)
    opening.configure(bg="mint cream")
    opening.title("Opening Balance")


    label_open=Label(opening,text="     Opening Amount",bg="mint cream",font=("Comic Sans MS", 13, "bold"),pady=10)
    label_open.grid(row=0,column=0,columnspan=2)

    label_note=Label(opening,text="Note : Enter the ammount you want to add",bg="mint cream",pady=10 )
    label_money=Label(opening,text="Enter The Ammount : ",bg="mint cream",font ="Times 12 italic bold",pady=10)

    label_money.grid(row=2,column=0)
    label_note.grid(row=1,columnspan=2,column=0)

    money=Entry(opening,width=25)
    money.grid(row=2,column=1)

    def Fconform():
        a=money.get()
        global l,u
        if(l==1):
            f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-savings-detailes.txt","a")
        else:
            f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-Current-detailes.txt","a")
        f1.write("Account Balace : "+a+" "+"\n")
        ans = datetime.today().strftime("%d-%m-%Y")
        f1.write(ans+" "+"+"+a+" "+a+" "+"\n")
        f1.close()
        opening.destroy()
        home()


    button_conform=Button(opening,text="Conform",command=Fconform,font=("Comic Sans MS", 13, "bold"), bg="tan", fg="royal blue")
    button_conform.grid(row=4,column=0,columnspan=2)

def password():
    password1=Tk()
    password1.title("Create Password")
    password1.geometry("350x580")
    password1.maxsize(350,580)
    password1.minsize(350,580)
    password1.configure(bg="mint cream")

    global k,l,u

    label_create=Label(password1,text="     Create your Password",bg="mint cream",font=("Comic Sans MS", 13, "bold"),pady=10)
    label_create.grid(row=0,column=0,columnspan=2)
    label_note=Label(password1,text="Note : Given below is your username save it for future use",bg="mint cream",pady=10)
    label_note.grid(row=1,column=0,columnspan=2)
    if(l==1):
        u="96"+k
        label_username= Label(password1,text="User Name : 96"+ k,bg="mint cream",font="Times 12 italic bold",pady=10)
        label_username.grid(row=2,column=0,columnspan=1)
    else:
        u = "97" + k
        label_username = Label(password1, text="User Name : 97" + k, bg="mint cream", font="Times 12 italic bold",pady=10)
        label_username.grid(row=2, column=0,columnspan=1)
    label_NewPassword = Label(password1, text="Password : ", bg="mint cream", font="Times 12 italic bold", pady=10)
    label_NewPassword.grid(row=3, column=0)
    label_ConformPassword = Label(password1, text="Conform Password :", bg="mint cream", font="Times 12 italic bold", pady=10)
    label_ConformPassword.grid(row=4, column=0)

    NewPassword=Entry(password1,width=25,show="*")
    ConformPassword=Entry(password1,width=25,show="*")

    NewPassword.grid(row=3,column=1)
    ConformPassword.grid(row=4,column=1)

    def check_special(char):
        check=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(check.search(char)== None):
            return False
        else:
            return True
    def Pconform():
        a=NewPassword.get()
        b=ConformPassword.get()
        if(a!=b):
            messagebox.showerror("Warning", "Password and Conform Password should be same")
        elif(len(a)<8):
            messagebox.showerror("Warning", "Password should contain atleast 8 Characters")
        elif(any(i.isalpha() for i in a) !=True or any(i.isdigit() for i in a) !=True or check_special(a)==False):
            messagebox.showerror("Warning", "Password should contain alphabets ,numbers and Special Characters")
        else:
            if(l==1):
                f1=open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-savings-detailes.txt","a")
            else:
                f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customers-Current-detailes.txt","a")
            f1.write("Stop \n\n\nUserName : "+ u+" "+" "+"\n")
            f1.write("Password : "+a+" "+" "+"\n")
            f1.close()
            password1.destroy()
            Opening_Ammount()

    button_conform=Button(password1,text="Conform", command=Pconform,font=("Comic Sans MS", 13, "bold"), bg="tan", fg="royal blue")
    button_conform.grid(row=5,column=0,columnspan=3)
    return


def signup1():
    app.destroy()
    signup=Tk()
    signup.title("Sign Up")
    signup.geometry('325x580')
    signup.minsize(325,580)
    signup.maxsize(325,580)
    signup.configure(bg="mint cream")

    global Fname, Mname, Lname, Dob,Pfname,Pmname,Nname,Address,adhar,pan,phno


    label_empty = Label(signup,text="      Fill the Detailes to proceed",bg="mint cream",font=("Comic Sans MS", 13, "bold"))
    label_empty.grid(row=0, column=0,columnspan=2)

    label_Fname=Label(signup,text='First Name : ',bg="mint cream",font="Times 12 italic bold",pady=10)
    label_Mname=Label(signup,text='Middle Name : ',bg="mint cream",font="Times 12 italic bold",pady=10)
    label_Lname = Label(signup, text='Last Name : ', bg="mint cream", font="Times 12 italic bold",pady=10)
    label_Dob = Label(signup, text='Date of Birth  : ', bg="mint cream", font="Times 12 italic bold",pady=10)
    label_Address = Label(signup, text='Address  : ', bg="mint cream", font="Times 12 italic bold",pady=10)
    label_Pfname= Label(signup, text='Father Name : ', bg="mint cream", font="Times 12 italic bold",pady=10)
    label_Pmname = Label(signup, text='Mother Name : ', bg="mint cream", font="Times 12 italic bold",pady=10)
    label_adhar = Label(signup, text='Adhar No : ', bg="mint cream", font="Times 12 italic bold",pady=10)
    label_pan = Label(signup, text='Pan No : ', bg="mint cream", font="Times 12 italic bold",pady=10)
    label_phno = Label(signup, text='Phone No : ', bg="mint cream", font="Times 12 italic bold",pady=10)
    label_Nname = Label(signup, text='Nominee Name : ', bg="mint cream", font="Times 12 italic bold",pady=10)

    label_Fname.grid(row=1,column=0)
    label_Mname.grid(row=2, column=0)
    label_Lname.grid(row=3, column=0)
    label_Dob.grid(row=4, column=0)
    label_Pfname.grid(row=5, column=0)
    label_Pmname.grid(row=6, column=0)
    label_Nname.grid(row=7, column=0)
    label_Address.grid(row=8, column=0)
    label_adhar.grid(row=9, column=0)
    label_pan.grid(row=10, column=0)
    label_phno.grid(row=11, column=0)

    Fname=Entry(signup,width=30)
    Mname=Entry(signup,width=30)
    Lname = Entry(signup, width=30)
    Dob = Entry(signup, width=30)
    Pfname = Entry(signup, width=30)
    Pmname = Entry(signup, width=30)
    Nname = Entry(signup, width=30)
    Address = Entry(signup, width=30)
    adhar = Entry(signup, width=30)
    pan = Entry(signup, width=30)
    phno = Entry(signup, width=30)


    Fname.grid(row=1,column=1)
    Mname.grid(row=2, column=1)
    Lname.grid(row=3, column=1)
    Dob.grid(row=4, column=1)
    Pfname.grid(row=5, column=1)
    Pmname.grid(row=6, column=1)
    Nname.grid(row=7, column=1)
    Address.grid(row=8, column=1)
    adhar.grid(row=9, column=1)
    pan.grid(row=10, column=1)
    phno.grid(row=11, column=1)


    r=IntVar()

    bubble_savings=Radiobutton(signup,text="Savings",variable=r,value=1,bg="mint cream",font="Times 12 italic bold")
    bubble_Current=Radiobutton(signup,text="Current",variable=r,value=2,bg="mint cream",font="Times 12 italic bold")

    bubble_savings.grid(row=12,column=0)
    bubble_Current.grid(row=12,column=1)


    def savingsA():
        savings=Tk()
        savings.title("Savings account")
        savings.geometry("350x580")
        savings.minsize(350,580)
        savings.maxsize(350,580)
        savings.configure(bg="mint cream")

        label_savings = Label(savings, text="Savings Account", font=("Comic Sans MS", 13, "bold"), pady=10,bg="mint cream")
        label_incometax = Label(savings, text="Do you pay income tax?",font="Times 12 italic bold",pady=10,bg="mint cream")
        label_occupation=Label(savings,text="Occupation : ",font="Times 12 italic bold",pady=10,bg="mint cream")
        label_monthly=Label(savings,text="Monthly Salary : ",font="Times 12 italic bold",pady=10,bg="mint cream")
        label_annual=Label(savings,text="Annual Income : ",font="Times 12 italic bold",pady=10,bg="mint cream")
        label_workplace=Label(savings,text="Work place Detailes :",font="Times 12 italic bold",pady=10,bg="mint cream")

        label_savings.grid(row=0,column=0,columnspan=2)
        label_occupation.grid(row=1, column=0)
        label_monthly.grid(row=2, column=0)
        label_annual.grid(row=3, column=0)
        label_workplace.grid(row=4,column=0)
        label_incometax.grid(row=5,column=0)


        Occupation=Entry(savings,width=28)
        monthly_salary=Entry(savings,width=28)
        Annual_income=Entry(savings,width=28)
        work_place=Entry(savings,width=28)

        Occupation.grid(row=1,column=1)
        monthly_salary.grid(row=2, column=1)
        Annual_income.grid(row=3, column=1)
        work_place.grid(row=4, column=1)

        s=StringVar()

        income_Yes= Radiobutton(savings,text="Yes",variable=s,value="Yes",bg="mint cream",font="Times 12 italic bold")
        income_No = Radiobutton(savings, text="No", variable=s, value="No",bg="mint cream",font="Times 12 italic bold")

        income_Yes.grid(row=5,column=1)
        income_No.grid(row=6, column=1)


        def Proceed1():
            a=Occupation.get()
            b=monthly_salary.get()
            c=Annual_income.get()
            d=work_place.get()
            f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customer-detailes.txt","a")
            f1.write("\nOccupation : "+a+"\n")
            f1.write("Monthly Salary : "+b+"\n")
            f1.write("Annual Income : "+c+"\n")
            f1.write("Work Place : "+d+"\n")
            f1.write("Income Tax : "+str(s.get())+"\n")
            f1.close()
            savings.destroy()
            password()

        Proceed=Button(savings,text="Proceed", font=("Comic Sans MS", 13, "bold"),bg="tan",fg="royal blue",command=Proceed1)
        Proceed.grid(row=7,column=0,columnspan=2)
        return

    def currentA():
        current=Tk()
        current.title("Current Account")
        current.geometry("350x580")
        current.minsize(350, 580)
        current.maxsize(350, 580)
        current.configure(bg="mint cream")

        label_Current = Label(current, text="Current Account", font=("Comic Sans MS", 13, "bold"), pady=10,bg="mint cream")
        label_CompanyName = Label(current, text="Company Name : ", font="Times 12 italic bold", pady=10,bg="mint cream")
        label_CompanyAddress = Label(current, text="Company Address : ", font="Times 12 italic bold", pady=10,bg="mint cream")
        label_AnnualTurnover = Label(current, text="Annual Income", font="Times 12 italic bold", pady=10,bg="mint cream")
        label_It = Label(current, text="It Amount :", font="Times 12 italic bold", pady=10,bg="mint cream")

        label_Current.grid(row=0,column=0,columnspan=2)
        label_CompanyName.grid(row=1,column=0)
        label_CompanyAddress.grid(row=2, column=0)
        label_AnnualTurnover.grid(row=3, column=0)
        label_It.grid(row=4, column=0)

        Company_Name = Entry(current, width=28)
        Company_Address = Entry(current, width=28)
        Annual_turnover = Entry(current, width=28)
        It = Entry(current, width=28)

        Company_Name.grid(row=1,column=1)
        Company_Address.grid(row=2, column=1)
        Annual_turnover.grid(row=3, column=1)
        It.grid(row=4, column=1)

        def Proceed1():
            a=Company_Name.get()
            b=Company_Address.get()
            c=Annual_turnover.get()
            d=It.get()
            f1 = open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customer-detailes.txt","a")
            f1.write("\nCompany Name : "+a+"\n")
            f1.write("Company Address : "+b+"\n")
            f1.write("Annual TurnOver: "+c+"\n")
            f1.write("It : "+d)
            f1.close()
            current.destroy()
            password()

        Proceed = Button(current, text="Proceed", font=("Comic Sans MS", 13, "bold"), bg="tan", fg="royal blue",command=Proceed1)
        Proceed.grid(row=5, column=0, columnspan=2)
        return

    def conform2():
        global k,l
        a=Fname.get()
        b=Mname.get()
        c=Lname.get()
        d=Dob.get()
        e=Pfname.get()
        f=Pmname.get()
        g=Nname.get()
        h=Address.get()
        i=adhar.get()
        j=pan.get()
        k=phno.get()
        l=r.get()
        f1=open(r"\Users\91984\Documents\KLH UNIVERSITY\PYTHON PROGRAMING\Files\Infinity Bank-Customer-detailes.txt","a")
        f1.write("\n\n\n")
        if(r.get()==1):
            f1.write("UserName : 96"+k+" "+"\n")
            f1.write("Account Type : " + "Savings Account" +" "+ "\n")
        else:
            f1.write("User Name : 97"+k+" "+"\n")
            f1.write("Account Type : " + "Current Account" + " "+"\n")
        f1.write("First Name : "+a+" "+"\n")
        f1.write("Middle Name : " + b + " "+"\n")
        f1.write("Last Name : " + c + " "+"\n")
        f1.write("FullName : " + a +" "+b+" "+c+" "+" "+"\n")
        f1.write("DOB : " + d + " "+"\n")
        f1.write("Father Name : " + e + " "+"\n")
        f1.write("Mother Name : " + f + " "+"\n")
        f1.write("Nominee Name : " + g + " "+"\n")
        f1.write("Address : " + h + " "+"\n")
        f1.write("Adhar No : " + i + " "+"\n")
        f1.write("Pan No : " + j + " "+"\n")
        f1.write("Phone No: " + k + " "+"\n")
        f1.close()
        signup.destroy()
        if(r.get()==1):
            savingsA()
        else:
            currentA()
        return

    def conform1():
        a = phno.get()
        b = adhar.get()
        if(len(a)!=10):
            messagebox.showerror("Warning","Enter correct number")
        elif(len(b)!=12):
            messagebox.showerror("Warning","Adhar no must 12 digits")
        else:
            conform2()
        return


    button_conform=Button(signup,text="Conform",command=conform1,font=("Comic Sans MS", 13, "bold"),bg="tan",fg="royal blue")
    button_conform.grid(row=13,column=0,columnspan=2)


    return



label_empty=Label(app,bg="mint cream")
label_empty.grid(row=2,column=1,pady=8)


label_empty1=Label(app,bg="mint cream")
label_empty1.grid(row=4,column=1)

button_login=Button(text="Login",command=login1,bg="mint cream",padx=25,pady=10,font="Times 15 italic bold")
button_signup=Button(text="Sign Up",command=signup1,bg="mint cream",padx=20,pady=10,font="Times 15 italic bold")

button_login.grid(row=3,column=1)
button_signup.grid(row=5,column=1)


app.mainloop()
