from tkinter import *
import tkinter as tk
from tkinter import ttk
from random import randint
from PIL import Image, ImageTk
from _datetime import datetime
from tkinter import scrolledtext

def grev():
   window = tk.Toplevel ()
   window.title ( "grievances" )
   window.config ( borderwidth=25, background="gray19" )
   window.state ( 'zoomed' )

   def complaintbox ():

      complaint1_file = open ( "complaint1.txt", 'a' )
      now = datetime.now ()
      date_time = now.strftime ( "%d/%m/%Y,%H:%M:%S" )
      complaint1_file.write ( date_time )
      complaint1_file.write ( '\n' )
      complaint1_file.write ( "Name of the account holder:"f'{name.get ()}\n' )
      complaint1_file.write ( "Account number of the account holder:"f'{account.get ()}\n' )
      complaint1_file.write ( "Complaint registered by the account holder:"f'{(complaint.get ())}\n' )

   canvas = tk.Canvas ( window, width=1440, height=720, background="#2e4a62" )
   canvas.pack ()
   img = ImageTk.PhotoImage ( Image.open ( "oop.gif" ) )
   canvas.create_image ( 350, 350, image=img )
   name_label = tk.Label ( window, text='ENTER YOUR FULL NAME', font=("times", 15, "bold") )
   name_label.place ( x=750, y=150 )

   name = tk.StringVar ()
   name_entry = tk.Entry ( window, font=("times", 15, "bold"), textvariable=name )
   name_entry.place ( x=1150, y=150 )

   account_label = tk.Label ( window, text="ENTER YOUR ACCOUNT NUMBER", font=("times", 15, "bold") )
   account_label.place ( x=750, y=250 )
   account = tk.StringVar ()
   account_entry = tk.Entry ( window, font=("times", 15, "bold"), textvariable=account )
   account_entry.place ( x=1150, y=250 )

   complaint_label = tk.Label ( window, text="ENTER YOUR COMPLAINT", font=("times", 15, "bold") )
   complaint_label.place ( x=950, y=350 )
   complaint = tk.StringVar ()
   complaint_entry = scrolledtext.ScrolledText ( window, font=("times", 15, "bold") )
   comp = complaint_entry.get ( "1.0", 'end' )

   complaint_entry.place ( width=500, height=200, x=850, y=400 )
   complaint_entry.focus ()

   submit_button = tk.Button ( window, font=("times", 15, "bold"), text="SUBMIT",command=complaintbox )
   submit_button.place ( x=1090, y=650 )

   window.mainloop ()

def disp_5():

    transaction=Toplevel()
    transaction.geometry("3000x3000")
    transaction.title("Transaction history")
    canvas = Canvas(transaction, width=3000, height=3000, background="skyblue")
    canvas.pack()
    imgt = ImageTk.PhotoImage(Image.open("transaction.png"))
    canvas.create_image(500, 750, anchor=S, image=imgt)
    title_label=Label(transaction,text="TRANSACTION HISTORY",font=("times", 30, "bold"),bg="skyblue")
    title_label.place(x=600, y=100)
    name_label = tk.Label(transaction, text='Your Last five Transaction Details:', font=("times",20, "bold"),bg="skyblue")
    name_label.place(x=800, y=250)
    myfile3=open(lid.get(),"r")
    contents=myfile3.readlines()
    label2 = Label ( transaction, text=f"{contents[10]}", font=("times", 20, "bold"), bg="skyblue" )
    label2.place ( x=800, y=370 )
    label3 = Label ( transaction, text=f"{contents[11]}", font=("times", 20, "bold"), bg="skyblue" )
    label3.place ( x=800, y=410 )
    label4 = Label ( transaction, text=f"{contents[12]}", font=("times", 20, "bold"), bg="skyblue" )
    label4.place ( x=800, y=450 )
    label5 = Label ( transaction, text=f"{contents[13]}", font=("times", 20, "bold"), bg="skyblue" )
    label5.place ( x=800, y=490 )
    label6 = Label ( transaction, text=f"{contents[14]}", font=("times", 20, "bold"), bg="skyblue" )
    label6.place ( x=800, y=530 )
    label7 = Label ( transaction, text=f"{contents[15]}", font=("times", 20, "bold"), bg="skyblue" )
    label7.place ( x=800, y=570 )



    transaction.mainloop()

def disp_10():
    transaction2=Toplevel()
    transaction2.geometry("3000x3000")
    transaction2.title("Transaction history")
    canvas = Canvas(transaction2, width=3000, height=3000, background="skyblue")
    canvas.pack()
    imgt = ImageTk.PhotoImage(Image.open("transaction.png"))
    canvas.create_image(500, 750, anchor=S, image=imgt)
    title_label=Label(transaction2,text="TRANSACTION HISTORY",font=("times", 30, "bold"),bg="skyblue")
    title_label.place(x=700, y=100)
    name_label = tk.Label(transaction2, text='Your Last ten Transaction Details:', font=("times",20, "bold"),bg="skyblue")
    name_label.place(x=1200, y=150)
    myfile3=open("credit3.txt","r")
    for i in reversed(range (30)):
        y = myfile3.readline()
        label2=Label(transaction2,text=f"{y}",font=("times",15, "bold"),bg="skyblue")
        label2.place(x=1200,y=160+(i+1)*25)
    transaction2.mainloop()

def transaction_win():
    k = Tk()
    k.geometry("300x150")
    k1 = Label(k, text='Transaction History', font="50")
    k1.pack()
    frame = Frame(k)
    frame.pack()
    bottomframe = Frame(k)
    bottomframe.pack(side=BOTTOM)
    k3 = Button(frame, text="Last 5", fg="red",command=disp_5)
    k3.pack(side=LEFT)
    k4 = Button(frame, text="Last 10", fg="brown",command=disp_10)
    k4.pack(side=LEFT)
    k5 = Button(frame, text="All", fg="blue")
    k5.pack(side=LEFT)
    k.mainloop()

def enquiry():
    balance=Toplevel()
    balance.geometry("600x300")
    balance.title("Balance")
    f2=open(lid.get(),"r")
    m=f2.readlines()
    bal=m[8].split()
    label_title=Label(balance,text=f"Your Account Balance is: {bal[1]}",font=("times", 30, "bold"),background="skyblue")
    label_title.place(x=35,y=100)
    balance.mainloop()


def creditw ():

    def credit_amt ():
        win1 = Toplevel ()
        win1.geometry ( "400x401" )
        win1.title ( "Confirmation" )
        imgs = ImageTk.PhotoImage ( Image.open ( "Success.png" ) )
        label = Label ( win1, image=imgs )
        label.image = imgs  # keep a reference!
        label.place ( x=0, y=0 )
        bimage = PhotoImage ( file="okay.png" )
        button1 = ttk.Button ( win1, image=bimage, width=73, command=creditw.destroy )
        button1.place ( x=140, y=300 )
        myfile = open ( lid.get(), "a" )
        myfile.write ( f"{name.get()}\n" )
        now = datetime.now ()
        date_time = now.strftime ( "%d/%m/%Y, %H:%M:%S" )
        myfile.write ( date_time + "\t \t +" + str ( k1.get () ) )
        myfile.close ()
        myfile2 = open ( lid.get(), "r" )
        p = myfile2.readlines ()
        b = p[8].split ()
        bn = int ( b[1] ) + int(k1.get())
        myfile2.close ()

        my = open ( lid.get(), "r" )
        data = my.read ()
        data = data.replace ( b[1], str ( bn ) )
        myfile2.close ()

        my = open ( lid.get(), "w" )
        my.write ( data )
        my.close ()


        win1.mainloop ()

    creditw = Tk ()
    creditw.geometry ( "600x600" )
    creditw.title ( "Credit Amount" )
    creditw.configure ( bg="ivory" )
    k = Label ( creditw, text="Enter Credit Amount" )
    k.place ( x=200, y=230 )
    cr = IntVar ()
    k1 = Entry ( creditw, width=28, textvariable=cr )
    k1.place ( x=200, y=250 )
    button = Button ( creditw, text="Confirm", width=8, command=credit_amt )
    button.place ( x=320, y=300 )
    button3 = Button ( creditw, text="Back", width=8 )
    button3.place ( x=320, y=350 )
    creditw.mainloop ()



def debit_win():

    def debit_amt ():

        myfile2 = open ( lid.get(), "r" )
        q = myfile2.readlines ()
        bal=q[8].split()

        print(k1.get())
        if int ( bal[1] ) < int(k1.get ()):
            error = Toplevel ()
            error.geometry ( "300x300" )
            error.title ( "Error" )
            error2 = Label ( error, text="ERROR" )
            error2.pack ()
            error3 = Label ( error, text="Enter valid amount" )
            error3.pack ()
            error.mainloop ()
        else:
            win2 = Toplevel ()
            win2.geometry ( "400x401" )
            win2.title ( "Confirmation" )
            imgs = ImageTk.PhotoImage ( Image.open ( "Success.png" ) )
            label = Label ( win2, image=imgs )
            label.image = imgs  # keep a reference!
            label.place ( x=0, y=0 )
            bimage = PhotoImage ( file="okay.png" )
            button2 = ttk.Button ( win2, image=bimage, width=73, command=debitw.destroy )
            button2.place ( x=140, y=300 )
            myfile2 = open ( lid.get(), "r" )
            q = myfile2.readlines ()
            bal = q[8].split ()
            myfile2.close ()
            bal[1] = int ( bal[1] ) - int(k1.get ())
            myfile = open ( "credit3.txt", "a" )
            myfile.write ( f'\nBalance amount:{q}\n' )
            myfile.close ()
            myfile2 = open ( "balance.txt", "w" )
            myfile2.write ( f"{q}" )
            myfile = open ( "credit3.txt", "a" )
            now = datetime.now ()
            date_time = now.strftime ( "%d/%m/%Y, %H:%M:%S" )
            myfile.write ( date_time + "\t \t -" + str ( db.get () ) )
            myfile.write ( "Mayaank\n" )
            myfile.close ()

            win2.mainloop ()

    debitw=Tk()
    debitw.geometry("600x600")
    debitw.title("Debit Amount")
    debitw.configure(bg="ivory")
    k=Label(debitw,text="Enter Debit Amount")
    db = IntVar ()
    k.place(x=200,y=230)
    k1=Entry(debitw,width=28,textvariable=db)
    k1.place(x=200,y=250)
    button=Button(debitw,text="Confirm",width=8,command=debit_amt)
    button.place(x=320,y=300)
    button2=Button(debitw,text="Back",width=8)
    button2.place(x=320,y=350)
    debitw.mainloop()



def main_menu ():

    myfile2 = open (lid.get(), "r" )
    p = myfile2.readlines ()
    myfile2.close ()
    n = p[2].split ()


    window = tk.Toplevel()
    window.title ( "main" )
    window.config ()
    window.state ( 'zoomed' )
    canvas = tk.Canvas ( window, width=1550, height=900, background="#2e4a62" )
    canvas.pack ()
    img = ImageTk.PhotoImage ( Image.open ( "transaction.jpg" ) )
    canvas.create_image ( 750, 400, image=img )
    credit_button = tk.Button ( window, font=("times", 15, "bold"), text="CREDIT", borderwidth=5, width=8,command=creditw)
    credit_button.place ( x=50, y=200 )

    debit_button = tk.Button ( window, font=("times", 15, "bold"), text="DEBIT", borderwidth=5, width=8 ,command=debit_win)
    debit_button.place ( x=50, y=550 )

    personalupdation_button = tk.Button ( window, font=("times", 15, "bold"),text='PERSONAL UPDATION', borderwidth=5,
                                 width=20 )
    personalupdation_button.place ( x=30, y=376.5 )

    transaction_button = tk.Button ( window, font=("times", 15, "bold"), text="TRANSACTION HISTORY", borderwidth=5,command=transaction_win,width=20 )
    transaction_button.place ( x=1225, y=185 )

    grievances_button = tk.Button ( window, font=("times", 15, "bold"), text="GRIEVANCES", borderwidth=5, width=15,command=grev)
    grievances_button.place ( x=1250, y=530 )

    balance_check = tk.Button ( window, font=("times", 15, "bold"), text='BALANCE ENQUIRY', borderwidth=5, width=20,command=enquiry )
    balance_check.place ( y=362, x=1225 )

    back_button = tk.Button ( window, font=("times", 15, "bold"), text="BACK", borderwidth=5, width=5, bg='gray39' )
    back_button.place ( x=10, y=730 )

    name_person = tk.Label ( window, font=("times", "24", "bold"), text=f"Welcome {n[2]} {n[3]} {n[4]}", bg='#E3E3E3', fg='black' )
    name_person.place ( x=550, y=30 )

    logout_button = tk.Button ( window, font=("times", 15, "bold"), text="LOGOUT", borderwidth=5, width=7, bg='gray39',command=logout )
    logout_button.place ( y=20, x=1425 )

    # time=tk.Frame(window,width=100,height=90)
    # time_option=tk.Label(time,text='Time')

    time_option = tk.Label ( font='Times 19 bold', bg='#ff8c00' )
    time_option.place ( x=25, y=30 )
    clock ( time_option )
    window.mainloop ()


def clock ( time_option ):
   date_time = datetime.datetime.now ().strftime ( "%d-%m-%Y %H:%M:%S/%p" )
   date, time1 = date_time.split ()
   time2, time3 = time1.split ( '/' )
   hour, minutes, seconds = time2.split ( ':' )
   if int ( hour ) > 11 and int ( hour ) < 24:
      time = str ( int ( hour ) - 12 ) + ':' + minutes + ':' + seconds + ' ' + time3
   else:
      time = time2 + ' ' + time3
   time_option.config ( text=time, fg='gray19' )
   time_option.after ( 1000, clock )


def display_window_2():

   file=open("login_ids.txt","r")
   contents=file.readlines()
   for line in contents :
      login_info = line.split()
      if k1.get() == login_info[0] and k2.get() == login_info[1]:
         main_menu()

def display_window_1():

   win1=tk.Tk()
   win1.config(width=360,height=360,background="#2e4a62")
   win1.title("Login Details")

   l1=Label(win1,text="Your account has been successfully created",font="Courier 13")
   l1.pack()

   l2 = Label(win1, text=f"Your Login ID: {r}", font="Courier 13")
   l2.pack()

   l3 = Label(win1, text="Kindly, secure this login ID for future", font="Courier 13")
   l3.pack(side=BOTTOM)

   f=open(str(r),"a")
   f.write("Login ID : " +str(r)+"\n")
   f.write("Password : "+ pwd.get()+"\n")
   f.write("Name : " + prefix.get()+" "+ name.get()+" "+lname.get()+"\n")
   f.write("DOB: "+day.get()+"/"+month.get()+"/"+year.get()+"\n")
   f.write("Address : "+ ad.get()+" "+ad1.get()+" "+ad3.get()+" "+ad4.get()+"\n")
   f.write("Pincode : "+pin.get()+"\n")
   f.write("Phone : " + ac.get()+" "+pn.get()+"\n")
   f.write("Email : "+em.get()+"\n")
   f.write("Balance: 1000\n")
   f.close()
   f=open("login_ids.txt","a")
   f.write(f"{r} {pwd.get()} \n")
   f.close()

window=tk.Tk()
window.geometry("3000x3000")
window.title("BANK MANAGEMENT SYSTEM")

frame1 = ttk.Frame( width=3000, height=3000)
frame2 = ttk.Frame( width=3000, height=3000)
frame3 = ttk.Frame( width=3000, height=3000 )
frame4 = ttk.Frame( width=3000, height=3000 )

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()

def change_to_frame32():
   frame3.pack( fill='both', expand=1 )
   frame4.pack_forget()

def change_to_frame4():
   frame4.pack( fill='both', expand=1 )
   frame3.pack_forget()

def change_to_frame3():
   frame3.pack( fill='both', expand=1 )
   frame2.pack_forget()

def change_to_frame2():
   frame2.pack(fill='both', expand=1)
   frame1.pack_forget()

def change_to_frame1():
   frame1.pack(fill='both', expand=1)
   frame3.pack_forget()

canvas = Canvas(frame1, width=3000, height=3000,background="black")
canvas.pack()
img1 = ImageTk.PhotoImage(Image.open("login.jpg"))
canvas.create_image(765, 850, anchor=S, image=img1)

canvas = Canvas(frame2, width=3000, height=3000,background="black")
canvas.pack()
imgx = ImageTk.PhotoImage(Image.open("SOP.png"))
canvas.create_image(765, 850, anchor=S, image=imgx)

canvas = Canvas( frame3, width=3000, height=3000, background="black" )
canvas.pack()
img = ImageTk.PhotoImage(Image.open("Form.png"))
canvas.create_image(768, 825, anchor=S, image=img)

canvas = Canvas( frame4, width=3000, height=3000, background="black" )
canvas.pack()
img3 = ImageTk.PhotoImage(Image.open("form2.png"))
canvas.create_image(768, 825, anchor=S, image=img3)


button_0=tk.Button( frame2, text="Click here for Account Opening Form",font=("Aharoni",18,"bold"), command=change_to_frame3,bg="black",fg="white",borderwidth=10 )
button_0.place(x=500,y=740)


lid=StringVar()
k1=tk.Entry(frame1,textvariable=lid,width=23,font=("century",20))
k1.place(x=615,y=305,height=59)

pwd=StringVar()
k2=tk.Entry(frame1,textvariable=pwd,width=23,font=("century",20),show="*")
k2.place(x=615,y=390,height=59)

limage=PhotoImage(file="login button.png")
button_9=ttk.Button(frame1,image=limage,width=20,command=display_window_2)
button_9.place(x=526,y=510)

simage=PhotoImage(file="signup.png")
button_3=ttk.Button(frame1,image=simage,width=10,command=change_to_frame2)
button_3.place(x=812,y=688)

prefix=StringVar()
k3 = Entry( frame3, bg="white", width=17, textvariable=prefix, font=("Didact Gothic", 25) )
k3.place(x=549,y=183)

name=StringVar()
k4 = Entry( frame3, bg="white", width=17, textvariable=name, font=("Didact Gothic", 25) )
k4.place(x=870,y=183)

lname=StringVar()
k5 = Entry( frame3, bg="white", width=17, textvariable=lname, font=("Didact Gothic", 25) )
k5.place(x=1191,y=183)

pwd=StringVar()
k6=Entry( frame3, textvariable=pwd, width=53, font=("Didact Gothic", 25),show="*" )
k6.place(x=547,y=420)

rpwd=StringVar()
k6=Entry( frame3, textvariable=rpwd, width=53, font=("Didact Gothic", 25),show="*" )
k6.place(x=547,y=522)

month=StringVar()
k7=Entry( frame4, textvariable=month, width=8, font=("Didact Gothic", 20) )
k7.place(x=35,y=60)

day=StringVar()
k8=Entry( frame4, textvariable=day, width=4, font=("Didact Gothic", 20) )
k8.place(x=166,y=60)

year=StringVar()
k8=Entry( frame4, textvariable=year, width=5, font=("Didact Gothic", 20) )
k8.place(x=233,y=60)

ac=StringVar()
k9=Entry( frame4, textvariable=ac, width=18, font=("Didact Gothic", 20) )
k9.place(x=550,y=160)

pn=StringVar()
k10=Entry( frame4, textvariable=pn, width=44, font=("Didact Gothic", 20) )
k10.place(x=840,y=160)

em=StringVar()
k11=Entry( frame4, textvariable=em, width=59, font=("Didact Gothic", 21) )
k11.place(x=550,y=265)

ad=StringVar()
k12=Entry( frame4, textvariable=ad, width=59, font=("Didact Gothic", 21) )
k12.place(x=550,y=365)

ad1=StringVar()
k13=Entry( frame4, textvariable=ad1, width=59, font=("Didact Gothic", 21) )
k13.place(x=550,y=440)

ad2=StringVar()
k14=Entry( frame4, textvariable=ad2, width=33, font=("Didact Gothic", 19) )
k14.place(x=549,y=513)

ad3=StringVar()
k15=Entry( frame4, textvariable=ad3, width=33, font=("Didact Gothic", 19) )
k15.place(x=1029,y=513)

ad4=StringVar()
k16=Entry( frame4, textvariable=ad4, width=33, font=("Didact Gothic", 19) )
k16.place(x=550,y=584)

pin=StringVar()
k17=Entry( frame4, textvariable=pin, width=33, font=("Didact Gothic", 19) )
k17.place(x=1029,y=584)

suimage=PhotoImage(file="submit.png")
button_5=tk.Button( frame4, image=suimage, command=display_window_1 )
button_5.place(x=5,y=690)

nimage=PhotoImage(file="next.png")
button_4=tk.Button( frame3, image=nimage, command=change_to_frame4 )
button_4.place(x=770,y=740)

bimage=PhotoImage(file="back.png")
button_6=tk.Button( frame4, image=bimage, command=change_to_frame32 )
button_6.place(x=30,y=781)

menu= StringVar()
menu.set("Select type of account")
drop= OptionMenu( frame3, menu, "Savings Account", "Current Account" )
drop.config(width=57,font=("Didact Gothic",22),background="white")
drop.place(x=547,y=323)

menu1= StringVar()
menu1.set("Gender")
drop1= OptionMenu( frame3, menu1, "Male", "Female", "Others" )
drop1.config(width=7,font=("Didact Gothic",31),background="white")
drop1.place(x=547,y=618)

range_start = 10**(10)
range_end = (10**11)-1
r=randint(range_start, range_end)
window.mainloop()
