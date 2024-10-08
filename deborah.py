import tkinter as tk
import tkinter.messagebox
import mysql.connector as sqlc

Un,Um,Ua,Us,Uc,Up,Uph,U,P="","","","","","","","",""
userloguser,passloguser="",""
screen=tk.Tk()
width=screen.winfo_screenwidth()
height=screen.winfo_screenheight()

screen.geometry("{0}x{1}+0+0".format(width,height))

screen["bg"]="white"
screen.title("Deborah")
tk.Label(screen, text="WELCOME TO DEBORAH BANKING",bg="#a4ac9c",width="1000",height="3",fg="White",font=("Britannic bold",40,'bold')).pack()

img =tk.PhotoImage(file='bg1.png')
tk.Label(screen, image=img, bg='white').place(x=60, y=180)

def ok(): #to close the self made pop-up message box window
    screen1.destroy()
    pop.destroy()

def clearallf():
    UnameEnt.delete(0,"end")
    UmailEnt.delete(0,"end")
    UaddEnt.delete(0,"end")
    UstateEnt.delete(0,"end")
    UcityEnt.delete(0,"end")
    UpinEnt.delete(0,"end")
    UphoneEnt.delete(0,"end")
    UserR_Ent.delete(0,"end")
    PassR_Ent.delete(0,"end")
    
def register_user():
    global screen1
    global Un,Um,Ua,Us,Uc,Up,Uph,U,P
    global cust
    conn=sqlc.connect(host="localhost",user="root",password="John@Maria@123",database="deborah")
    cursor=conn.cursor()
    Un=UnameEnt.get()
    Um=UmailEnt.get()
    Ua=UaddEnt.get()
    Us=UstateEnt.get()
    Uc=UcityEnt.get()
    Up=UpinEnt.get()
    Uph=UphoneEnt.get()
    U=UserR_Ent.get()
    P=PassR_Ent.get()
    amt=0
    cursor.execute("select UserR from Udetails")
    r=cursor.fetchall()

    n=len(r)
    lov=list() #List of values (users)
    for i in range(n):
        val=r[i][0]
        valt=val.upper()
        lov.append(valt)   
        
    use=U.upper()
   
    
    if Un=="" or Um==""  or Ua==""  or Us==""  or Uc==""  or Up==""  or Uph==""  or U==""  or P=="" :
        tk.messagebox.showwarning("Error","All fields are required",parent=screen1)
        
    elif len(Up)>6 or len(Up)<6 or Up[0]=='0' or Up.isnumeric()==False:
        tk.messagebox.showwarning("Error","Invalid pincode",parent=screen1)
        
    elif len(Uph) < 10 or Uph.isnumeric()==False:
        tk.messagebox.showwarning("Error","Invalid phone number",parent=screen1)
    
    elif U.isalnum()==False:
        tk.messagebox.showwarning("Error","Username should not contain special characters or whitespaces",parent=screen1)
    
    elif U[0].isnumeric()==True:
          tk.messagebox.showwarning("Error","Username should not start with a number",parent=screen1)
        
    elif use in lov:
        tk.messagebox.showwarning("Error","This username is already taken away please try something new !",parent=screen1)
    
    elif P.isalpha()==True:
        tk.messagebox.showwarning("Error","Enter a password containing both alphabets and numerical values",parent=screen1)
        
    elif len(P) <8:
        tk.messagebox.showwarning("Error","Password must contain at least 8 characters",parent=screen1)


    else:
        cursor.execute("select max(custId) from Udetails")
        records=cursor.fetchall()
        max=records[0][0]
        if max is None:
            cust=1
            #Utable=U+str(cust)
        else:
         
            cust=max+1           #uniquecustomer id
            #Utable=U+str(cust)

        cursor.execute("CREATE TABLE IF NOT EXISTS Usdetails (Uname varchar(200), Umail varchar(250), Uadd text, Ustate varchar(100), Ucity varchar(200), Upin varchar(7), Uphone varchar(15), UserR text, PassR text,custId int primary key,Amount double)")
        conn.commit()
        cursor.execute("insert into Udetails values ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{})".format(Un,Um,Ua,Us,Uc,Up,Uph,U,P,cust,amt))
        conn.commit()
        conn.close()
        
        
    
        global pop
        pop=tk.Toplevel()
        pop.title("Done")
        pop.geometry("250x150+200+300")
        #pop.iconbitmap("MainLogo.ico")
        #tick=tk.PhotoImage(file="RegTick.png")
        fr=tk.Frame(pop,bg="white")
        fr.place(x=0,y=0,height=150,width=250)
        print("\a")
        back_label=tk.Label(fr,bg="white")
        back_label.place(relheight=1,relwidth=1)  
        l=tk.Label(fr,text="Your Registration is successful !",font=("times new roman",13,"bold"),bg="white")
        l.place(x=0,y=10)
        butn=tk.Button(fr,text="OK",bg="green",fg="white",font=("times new roman",12),width=7,command=ok)
        butn.place(x=85,y=105)



def register():
    global back_image
    global userReguser
    global passReguser
    global screen1
    global UnameEnt, UmailEnt, UaddEnt, UstateEnt, UcityEnt, UpinEnt, UphoneEnt, UserR_Ent, PassR_Ent 
    screen1= tk.Toplevel()
    screen1.title("Register")
    screen1.geometry("{0}x{1}+0+0".format(width,height))
    
    frame=tk.Frame(screen1,bg="#EAE87C")               
    frame.place(x=0,y=0,height=height,width=width)
    
   
    
    au_frame=tk.Frame(frame,bg="white")
    au_frame.place(x=810,y=50,height=700,width=500)
    tit=tk.Label(au_frame,text="About Us",bg="white",font=("impact",35,"bold"),fg="#d77337")
    tit.place(x=160,y=10)    
    tk.Label(au_frame,bg="white",text="Your trust in us is the driving force behind everything we do",font=("times new roman",14)).place(x=0,y=110)
    tk.Label(au_frame,bg="white",text="we wanted to take a moment to express our sincere gratitude ",font=("times new roman",14)).place(x=0,y=140)
    tk.Label(au_frame,bg="white",text="for choosing us as your trusted financial partner.",font=("times new roman",14)).place(x=0,y=170)
    tk.Label(au_frame,bg="white",text="In today's fast-paced world, we understand that your time is are of ",font=("times new roman",14)).place(x=0,y=200)
    tk.Label(au_frame,bg="white",text="paramount importance that’s why we ensure that your banking ",font=("times new roman",14)).place(x=0,y=230)
    tk.Label(au_frame,bg="white",text="experience is not just efficient but also tailored to your unique",font=("times new roman",14)).place(x=0,y=260)
    tk.Label(au_frame,bg="white",text="needs and aspirations.",font=("times new roman",14)).place(x=0,y=290)
    tk.Label(au_frame,bg="white",text="Your feedback is invaluable to us.",font=("times new roman",14)).place(x=0,y=370)
    tk.Label(au_frame,bg="white",text="We are committed to listening to your suggestions and concerns,",font=("times new roman",14)).place(x=0,y=400)
    tk.Label(au_frame,bg="white",text="and we continually strive to enhance our services",font=("times new roman",14)).place(x=0,y=430)
    tk.Label(au_frame,bg="white",text="to better serve you. Your voice shapes the future of our bank,",font=("times new roman",14)).place(x=0,y=460)
    tk.Label(au_frame,bg="white",text="and together, we will continue to build a banking experience",font=("times new roman",14)).place(x=0,y=490)
    tk.Label(au_frame,bg="white",text="that exceeds your expectations.",font=("times new roman",14)).place(x=0,y=520)
    tk.Label(au_frame,bg="white",text="and we continually strive to enhance our services",font=("times new roman",14)).place(x=0,y=550)
    
    r_frame=tk.Frame(frame,bg="white")
    r_frame.place(x=140,y=50,height=700,width=500)

    title=tk.Label(r_frame,text="Register here",bg="white",font=("impact",35,"bold"),fg="#d77337")
    title.place(x=100,y=10)
    title=tk.Label(r_frame,text="* All fields are required",bg="white",fg="red",font=("times new roman",14,"bold"))
    title.place(x=10,y=70)
  
    Uname=tk.Label(r_frame,text="Enter Your Name",bg="white",font=("times new roman",15,"bold"),fg="gray")
    Uname.place(x=10,y=110)
        
    UnameEnt=tk.Entry(r_frame,font=("calibri",15),bg="#EEEEE9")
    UnameEnt.place(x=190,y=110)
    
    Umail=tk.Label(r_frame,text="Enter Email Id",bg="white",font=("times new roman",15,"bold"),fg="gray")
    Umail.place(x=10,y=150)
    
    UmailEnt=tk.Entry(r_frame,font=("calibri",15),bg="#EEEEE9")
    UmailEnt.place(x=190,y=150)
    
    Uadd=tk.Label(r_frame,text="Enter Your Address",bg="white",font=("times new roman",15,"bold"),fg="gray")
    Uadd.place(x=10,y=190)
    
    UaddEnt=tk.Entry(r_frame,font=("calibri",15),bg="#EEEEE9")
    UaddEnt.place(x=190,y=190)
    
    Ustate=tk.Label(r_frame,text="Enter State",bg="white",font=("times new roman",15,"bold"),fg="gray")
    Ustate.place(x=10,y=230)
    
    UstateEnt=tk.Entry(r_frame,font=("calibri",15),bg="#EEEEE9")
    UstateEnt.place(x=190,y=230)
    
    Ucity=tk.Label(r_frame,text="Enter City",bg="white",font=("times new roman",15,"bold"),fg="gray")
    Ucity.place(x=10,y=270)
    
    UcityEnt=tk.Entry(r_frame,font=("calibri",15),bg="#EEEEE9")
    UcityEnt.place(x=190,y=270)
    
    Upin=tk.Label(r_frame,text="Pin-Code",bg="white",font=("times new roman",15,"bold"),fg="gray")
    Upin.place(x=10,y=310)
    
    UpinEnt=tk.Entry(r_frame,font=("calibri",15),bg="#EEEEE9")
    UpinEnt.place(x=190,y=310)
    
    Uphone=tk.Label(r_frame,text="Phone-Number",bg="white",font=("times new roman",15,"bold"),fg="gray")
    Uphone.place(x=10,y=350)
    
    UphoneEnt=tk.Entry(r_frame,font=("calibri",15),bg="#EEEEE9")
    UphoneEnt.place(x=190,y=350)

    UserR=tk.Label(r_frame,text="Username",bg="white",font=("times new roman",15,"bold"),fg="gray")
    UserR.place(x=10,y=390)

    UserR_Ent=tk.Entry(r_frame,font=("calibri",15),bg="#EEEEE9")
    UserR_Ent.place(x=190,y=390)

    PassR=tk.Label(r_frame,text="Password",bg="white",font=("times new roman",15,"bold"),fg="gray")
    PassR.place(x=10,y=430)

    PassR_Ent=tk.Entry(r_frame,font=("calibri",15),bg="#EEEEE9")
    PassR_Ent.place(x=190,y=430)
    
    reg_button=tk.Button(r_frame,text="Register",font=("times new roman",20),bg="#d77337",fg="white",width=13,cursor="hand2",command=register_user)
    reg_button.place(x=10,y=590)
    
    clearall=tk.Button(r_frame,text="Click here to clear all fields",font=("times new roman",12),cursor="hand2",fg="#d77337",bg="white",bd=0,command=clearallf)
    clearall.place(x=10,y=650)



def deposit(): #Deposit functionality
    global userDash
    deposit=user.get()
    conn=sqlc.connect(host="localhost",user="root",password="John@Maria@123",database="Deborah")
    cursor=conn.cursor()
    cursor.execute("select amount from udetails where userR='{}' ".format(userDash))
    bal1=cursor.fetchall()
    balance=bal1[0][0]
    try:
        total=balance+float(deposit)
        user.delete(0,"end")
    except ValueError :
        tk.messagebox.showwarning("Error", "Enter appropriate amount",parent=root2)
        total=balance+0
        user.delete(0,"end")
        
    #t="Your current Balance is : "+str(total)
    #curB.config(text=t)
    cursor.execute("Update udetails set amount = {} where userR= '{}' ".format(total,userDash))
    conn.commit()
    tk.messagebox.showinfo("Success","Amount successfully deposited",parent=root2)  
    conn.close()
    root2.destroy()
    
def depo(): #Design of deposit
    global user
    global root2
    root2=tk.Toplevel()
    root2.title('deposit')
    root2.geometry('925x500+300+200')
    root2.configure(bg="#fff")
    root2.resizable (False, False)
    img =tk.PhotoImage(file='dep.png')
    tk.Label(root2, image=img, bg='white').place(x=50, y=50)
    frame=tk.Frame (root2, width=350,height=350, bg="white")
    frame.place(x=480,y=70)
    heading =tk.Label (frame, text='Deposit Amount here', fg='#E68B88', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) 
    heading.place(x=24,y=5)
    user =tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=100)
    tk.Frame (frame, width=295,height=2, bg='black').place(x=25,y=140)
    tk.Button(frame,width=39, pady=7, text='Deposit', bg='#E68B88', fg='white', cursor="hand2", border= 0, command=deposit).place(x=35, y=204)
    root2.mainloop()
    
def withdraw(): #Deposit functionality
    global userDash
    val=float(value.get())
    conn=sqlc.connect(host="localhost",user="root",password="John@Maria@123",database="Deborah")
    cursor=conn.cursor()
    cursor.execute("select amount from udetails where userR='{}' ".format(userDash))
    bal1=cursor.fetchall()
    balance=bal1[0][0]
    
    if (balance-val)<0:
        tk.messagebox.showwarning("Insufficient Funds","Insuffient money in account",parent=root1)
    elif (balance-val)>=0:
        total=balance-val
        cursor.execute("Update udetails set amount = {} where userR= '{}' ".format(total,userDash))
        conn.commit()
        conn.close()
        value.delete(0,"end")
        tk.messagebox.showinfo("Success","Amount successfully Withdrawed",parent=root1)
        
    else:
        tk.messagebox.showwarning("Error","An error occurred ",parent=root1)
    
    root1.destroy()
     
def withu(): #Design of deposit
    global value
    global root1
    root1=tk.Toplevel()
    root1.title('Withdrawl')
    root1.geometry('925x500+300+200')
    root1.configure(bg="#fff")
    root1.resizable (False, False)
    img =tk.PhotoImage(file='img2.png')
    tk.Label(root1, image=img, bg='white').place(x=0, y=40)
    frame=tk.Frame (root1, width=350,height=350, bg="white")
    frame.place(x=480,y=70)
    heading =tk.Label (frame, text='Enter Amount here', fg='#E68B88', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) 
    heading.place(x=24,y=5)
    value=tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
    value.place(x=30,y=110)
    tk.Frame (frame, width=295,height=2, bg='black').place(x=25,y=140)
    tk.Button(frame,width=39, pady=7, text='Withdraw', bg='#E68B88', fg='white', border= 0, cursor="hand2", command=withdraw).place(x=35, y=204)
    root1.mainloop() 

def balance(): #Deposit functionality
    global userDash
   
    conn=sqlc.connect(host="localhost",user="root",password="John@Maria@123",database="Deborah")
    cursor=conn.cursor()
    cursor.execute("select amount from udetails where userR='{}' ".format(userDash))
    bal1=cursor.fetchall()
    balance=bal1[0][0]
        
    t=str(balance)
    bal =tk.Label (frame2, text=t, fg='#E68B88', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) 
    bal.place(x=24,y=90)
    #curB.config(text=t)
    conn.close()
      
def balu(): #Design of deposit
    global user
    global root
    global frame2
    root=tk.Toplevel()
    root.title('Check Balance')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable (False, False)
    img =tk.PhotoImage(file='pic.png')
    tk.Label(root, image=img, bg='white').place(x=50, y=40)
    frame2=tk.Frame (root, width=350,height=350, bg="white")
    frame2.place(x=480,y=70)
    heading =tk.Label (frame2, text='Your Balance is :', fg='#E68B88', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) 
    heading.place(x=24,y=5)
    
    tk.Frame (frame2, width=295,height=2, bg='black').place(x=25,y=140)
    tk.Button(frame2,width=39, pady=7, text='Check Balance', bg='#E68B88', fg='white', border= 0,cursor="hand2", command=balance).place(x=35, y=204)
    root.mainloop()
  
def bank(userlog_info):
    global screen3
    global cart
    global back_reg
    global userDash
    userDash = userlog_info
    screen3=tk.Toplevel()
    screen3.title("Deborah Bank")
    screen3.geometry("{0}x{1}+0+0".format(width,height))
    
    conn=sqlc.connect(host="localhost",user="root",password="John@Maria@123",database="deborah")
    cursor=conn.cursor()
    frame1=tk.Frame(screen3,bg="white")
    frame1.place(x=0,y=0,width=width,height=height)
    
    frame2=tk.Frame(frame1,bg="#397397")
    frame2.place(x=0,y=0,width=width,height=60)
    
    l=userlog_info
    cursor.execute("select Uname from Udetails where UserR = '{}'".format(l))
    records=cursor.fetchall()
    text="Hello "+records[0][0]+","
    
    hello1=tk.Label(frame2,text=text,font=("verdana",17),bg="#397397",fg="white")
    hello1.place(x=5,y=10)    
    
    text=tk.Label(screen3,text="Click any one of the following options to avail it's services",font=("verdana",17),fg="#364049", bg="white")
    text.place(x=10,y=65)
    
    dep=tk.Button(screen3,text="Deposit",bg="#C9E5F8",font=("impact",35,"bold"),fg="#397397",cursor="hand2", bd=0, command=depo)
    dep.place(x=40 ,y=200 ,height=340,width=450)
    
    withi=tk.Button(screen3,text="Withdraw",bg="#C9E5F8",font=("impact",35,"bold"),fg="#397397",cursor="hand2", bd=0, command=withu)
    withi.place(x=540 ,y=200 ,height=340,width=450)
    
    chk_bal=tk.Button(screen3,text="Check Balance",bg="#C9E5F8",font=("impact",35,"bold"),fg="#397397",cursor="hand2", bd=0, command=balu)
    chk_bal.place(x=1040 ,y=200 ,height=340,width=450)
    

def login():
    global userloguser
    global passloguser
    global userlog_info
    global passlog_info
    conn=sqlc.connect(host="localhost",user="root",password="John@Maria@123",database="deborah")
    cursor=conn.cursor()
    
    userlog_info=userloguser.get()
    passlog_info=passloguser.get()
    
    passloguser.delete(0,"end")
    userloguser.delete(0,"end")
    
    cursor.execute("select UserR,PassR from Udetails where UserR='{0}' and PassR='{1}'".format(userlog_info,passlog_info))
    records=cursor.fetchall()
    
    if userlog_info=="" or passlog_info=="":
       tk.messagebox.showwarning("Error","All fields are required")
         
    elif len(records)==1:
         if userlog_info==records[0][0] and passlog_info==records[0][1]:
            bank(userlog_info)
            conn.close()
         else:
            tk.messagebox.showwarning("Error","Invalid details!") 
        
    else :
        tk.messagebox.showwarning("Error","Invalid details!")
        
    conn.close()   
    
  





lr_frame=tk.Frame(screen,bg="white")
lr_frame.place(x=950,y=320,height=340,width=500)

title=tk.Label(lr_frame,text="Sign In",bg="white",font=("Times New Roman",35,'bold'),fg="#b79a6e")
title.place(x=130,y=10)

userL=tk.Label(lr_frame,text="Username",bg="white",font=("Times New Roman",15,"bold"),fg="#3C484F")
userL.place(x=133,y=80)

astL=tk.Label(lr_frame,text="*",bg="white",font=("Times New Roman",15,"bold"),fg="red")
astL.place(x=225,y=80)

userloguser=tk.Entry(lr_frame,font=("Calibri",15),bg="#EEEEE9")
userloguser.place(x=133,y=110)

passL=tk.Label(lr_frame,text="Password",bg="white",font=("Times New Roman",15,"bold"),fg="#3C484F")
passL.place(x=133,y=140)

astR=tk.Label(lr_frame,text="*",bg="white",font=("Times New Roman",15,"bold"),fg="red")
astR.place(x=225,y=140)

passloguser=tk.Entry(lr_frame,font=("Calibri",15),bg="#EEEEE9",show="*")
passloguser.place(x=133,y=170)

Log_button=tk.Button(lr_frame,text="Sign In",font=("Lucida Bright",15,'bold'),bg="#93AF9D",cursor="hand2",fg="#425649",width=13,command=login)
Log_button.place(x=133,y=210)

reg=tk.Button(lr_frame,text="Not Yet Registered ? Click Here to Register",font=("Times New Roman",12,'bold'),cursor="hand2",fg="#b79a6e",bg="white",bd=0,command=register)
reg.place(x=90,y=270)


screen.mainloop()
