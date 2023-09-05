from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter import Button

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()
    

class login_window():
    def __init__(self,root):
        self.root=root
        self.root.title('Login Page')
        self.root.geometry('1600x790+0+0')
        
        #........................variables...................

        self.user_var = StringVar()
        self.email_var = StringVar()
        
        #.................Images...................
        self.bg=ImageTk.PhotoImage(file='hospital.jpg')
        bg_lbl=Label(self.root,image=self.bg,bd=12,relief=RAISED)
        bg_lbl.place(x=0,y=0,relwidth=1)

        logo_img=Image.open('C:\PHARMA\log.jpg.jpg')
        logo_img=logo_img.resize((60,60),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)

        # Title frame
        title_frame=Frame(self.root,bd=1,relief=RIDGE)
        title_frame.place(x=450,y=28,width=546,height=82)

        title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text='User Login Form',font=("times new roman",32,"bold"),fg='darkblue')
        title_lbl.place(x=10,y=10)
        
        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=110,width=546,height=500)

        # UserName

        user_name=Label(main_frame,text='Email:',font=('times new roman',16,'bold'))
        user_name.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        user_txt=ttk.Entry(main_frame,textvariable=self.user_var,font=('arial',16,'bold'),width=25)
        user_txt.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        email_name=Label(main_frame,text='Password:',font=('times new roman',16,'bold'))
        email_name.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        email_txt=ttk.Entry(main_frame,textvariable=self.email_var,font=('arial',16,'bold'),width=25)
        email_txt.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #.....................................Buttons.....................................
        button_frame=Frame(self.root,bd=1,relief=RIDGE)
        button_frame.place(x=450,y=550,width=546,height=60)
        #.........................Buttons.................
        self.btnAddmed = Button(button_frame,command=self.register_btn,text="Register", font=("arial", 15, "bold"), width=13, bg="lime", fg="white", pady=4, padx=2)
        self.btnAddmed.grid(row=0,column=0)

        btnUpdatemed = Button(button_frame,command=self.login_btn,text="Login",font=("arial",15,"bold"),width=16,bg="purple",fg="white",pady=4,padx=2)
        btnUpdatemed.grid(row=0,column=3)

        btnDeletemed = Button(button_frame,text="Clear",font=("arial",15,"bold"),width=13,bg="red",fg="white",pady=4,padx=2)
        btnDeletemed.grid(row=0,column=5)
      #...................Navigating functions...............................  
    def register_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login_btn(self):
        if self.user_var.get()=="" or self.email_var.get()=="":
            messagebox.showerror("error","all fields required")
        elif self.user_var.get()=="bzet@gmail.com" and self.email_var.get()=="bzet22":
            
            self.new_window=Toplevel(self.root)
            self.app=PharmacyManagementSystem(self.new_window)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.user_var.get(),
                                                                                    self.email_var.get()
                                                                                        ))
            row=my_cursor.fetchone()
            if row ==None:
                messagebox.showerror("Error","Invalid username and password") 
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                          
                    self.new_window=Toplevel(self.root)
                    self.app=PharmacyManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


class Register():
    def __init__(self,root):
        self.root=root
        self.root.title('Register Page')
        self.root.geometry('1600x790+0+0')
        

#........................variables...................

        self.user_var = StringVar()
        self.email_var = StringVar()
        self.contact_var = StringVar()
        self.gender_var = StringVar()
        self.type_var = StringVar()
        self.id_var = StringVar()
        self.password_var = StringVar()
        self.confpassword_var = StringVar()

#.................Images...................
        self.bg=ImageTk.PhotoImage(file='hospital.jpg')
        bg_lbl=Label(self.root,image=self.bg,bd=12,relief=RAISED)
        bg_lbl.place(x=0,y=0,relwidth=1)

        logo_img=Image.open('C:\PHARMA\log.jpg.jpg')
        logo_img=logo_img.resize((60,60),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)

        # Title frame
        title_frame=Frame(self.root,bd=1,relief=RIDGE)
        title_frame.place(x=450,y=28,width=546,height=82)

        title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text='User Registration Form',font=("times new roman",32,"bold"),fg='darkblue')
        title_lbl.place(x=10,y=10)


        #.........................Information Frame..............................

        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=110,width=546,height=500)

        # UserName

        user_name=Label(main_frame,text='Username:',font=('times new roman',16,'bold'))
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        user_txt=ttk.Entry(main_frame,textvariable=self.user_var,font=('arial',16,'bold'),width=25)
        user_txt.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        email_name=Label(main_frame,text='Email:',font=('times new roman',16,'bold'))
        email_name.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        email_txt=ttk.Entry(main_frame,textvariable=self.email_var,font=('arial',16,'bold'),width=25)
        email_txt.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        contact_name=Label(main_frame,text='Contact No:',font=('times new roman',16,'bold'))
        contact_name.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        contact_txt=ttk.Entry(main_frame,textvariable=self.contact_var,font=('arial',16,'bold'),width=25)
        contact_txt.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        gender_name=Label(main_frame,text='Select Gender:',font=('times new roman',16,'bold'))
        gender_name.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(main_frame,textvariable=self.gender_var, width=23,font=("arial",16,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.grid(row=3,column=1)
        gender_combo.current(0)

        idType_name=Label(main_frame,text='Select ID Type:',font=('times new roman',16,'bold'))
        idType_name.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        idType_txt=ttk.Entry(main_frame,textvariable=self.type_var,font=('arial',16,'bold'),width=25)
        idType_txt.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        idNo_name=Label(main_frame,text='ID Number:',font=('times new roman',16,'bold'))
        idNo_name.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        idNo_txt=ttk.Entry(main_frame,textvariable=self.id_var,font=('arial',16,'bold'),width=25)
        idNo_txt.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        password_name=Label(main_frame,text='Password:',font=('times new roman',16,'bold'))
        password_name.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        password_txt=ttk.Entry(main_frame,textvariable=self.password_var,font=('arial',16,'bold'),width=25)
        password_txt.grid(row=7,column=1,padx=10,pady=10,sticky=W)

        confPassword_name=Label(main_frame,text='Confirm Password:',font=('times new roman',16,'bold'))
        confPassword_name.grid(row=8,column=0,padx=10,pady=10,sticky=W)
        confPassword_txt=ttk.Entry(main_frame,textvariable=self.confpassword_var,font=('arial',16,'bold'),width=25)
        confPassword_txt.grid(row=8,column=1,padx=10,pady=10,sticky=W)

#.....................................Buttons.....................................
        button_frame=Frame(self.root,bd=1,relief=RIDGE)
        button_frame.place(x=450,y=550,width=546,height=60)
        #.........................Buttons.................
        self.btnAddmed = Button(button_frame, text="Register", font=("arial", 15, "bold"), width=13, bg="lime", fg="white", pady=4, padx=2,command=self.register)
        self.btnAddmed.grid(row=0,column=0)

        btnUpdatemed = Button(button_frame,text='Add',font=("arial",15,"bold"),width=16,bg="purple",fg="white",pady=4,padx=2)
        btnUpdatemed.grid(row=0,column=3)

        btnDeletemed = Button(button_frame,text="Clear",font=("arial",15,"bold"),width=13,bg="red",fg="white",pady=4,padx=2,command=self.clear)
        btnDeletemed.grid(row=0,column=5)
#.................................Button Functionality...............................
    def register(self):
        print("AddMed method invoked")
        if self.password_var.get() == "" or self.user_var.get()=="":
                messagebox.showerror("Error","All fields are required and check password if it is the same")
        else:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into register(user_name, email, contact, gender, user_type, user_id, password) values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                self.user_var.get(),
                                                                                self.email_var.get(),
                                                                                self.contact_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.type_var.get(),
                                                                                self.id_var.get(),
                                                                                self.password_var.get()
                                                                                
                                                                     ))

        conn.commit()
        conn.close()
        messagebox.showinfo("Successfully","Registered")
        
        
    def clear(self):
        
        self.user_var.set(""),
        self.email_var.set(""),
        self.contact_var.set(""),
        self.gender_var.set(""),
        self.type_var.set(""),
        self.id_var.set(""),
        self.password_var.set("")
        

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()




class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

#........................Add Variables............................
        self.refMed_var = StringVar()
        self.Addmed_var = StringVar()

#........................Main Table Varieble...........................

        self.ref_var = StringVar()
        self.cmpName_var = StringVar()
        self.typeMed_var = StringVar()
        self.medName_var = StringVar()
        self.lot_var = StringVar()
        self.issueDate_var = StringVar()
        self.expDate_var = StringVar()
        self.uses_var = StringVar()
        self.sideEffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.product_var = StringVar()
        
        lbltitle=Label(self.root,text="Pharmacy Management System",bd=15,relief=RIDGE
                            ,bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        
        lbltitle.pack(side=TOP,fill=X)
#....................Logo.............................
        img = Image.open("C:\PHARMA\logo.png.png")
        img = img.resize((80,80), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)

#.......................Data Frame..................
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1365,height=385)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                 fg="darkgreen",font=("Arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=730,height=350)

        
#.......................Button Frame.................
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=510,width=1290,height=50)
#.....................Main Button....................
        btnAddData=Button(ButtonFrame,text="Medicine Add",command=self.add_data,font=("Arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,text="Update",command=self.update_Med,font=("Arial",12,"bold"),width=10,bg="blue",fg="white")
        btnUpdateMed.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,text="Delete",command=self.deleteMed,font=("Arial",12,"bold"),width=10,bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)

        btnResetMed=Button(ButtonFrame,text="Reset",command=self.reset,font=("Arial",12,"bold"),width=10,bg="powderblue",fg="white")
        btnResetMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,text="Exit",font=("Arial",12,"bold"),width=10,bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)
#............................Searrch By.........................
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"), text="Search By", padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)
#.........................searching variable............................................................

        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",13,"bold"))
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        
        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",16,"bold"))
        txtSearch.grid(row=0,column=7)

        searchBtn=Button(ButtonFrame,command=self.search_data,text="Search",font=("Arial",13,"bold"),width=12,bg="powderblue",fg="white")
        searchBtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,command=self.fetch_data,text="Show All",font=("Arial",13,"bold"),width=12,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)

        #..........................Label and Entry.....................

        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2,pady=6)
        lblrefno.grid(row=0,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var, width=18,font=("arial",13,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        lblCmpName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=20)
        txtCmpName.grid(row=1,column=1)

        lblTypeOfMedicine = Label(DataFrameLeft,font=("arial",12,"bold"), text="Type of Medicine:",padx=2,pady=6)
        lblTypeOfMedicine.grid(row=2,column=0,sticky=W)

        comTypeOfMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,state="readonly",
                                       font=("arial",12,"bold"),width=18)
        
        comTypeOfMedicine['value']=("Tablet","Liquid","Topical","Drop","Inhales","Injection")
        comTypeOfMedicine.current(0)
        comTypeOfMedicine.grid(row=2,column=1)

        #.....................adding Medicine..............
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med=my_cursor.fetchall()

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,state="readomnly",
                                     font=("arial",12,"bold"),width=18)
        comMedicineName["values"]=("vitamin d","vitamin anc")
        comMedicineName.grid(row=3,column=1)
        comMedicineName.current(0)

        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issueDate_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtIssueDate.grid(row=5,column=1)

        lblExpireDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expire Date:",padx=2,pady=6)
        lblExpireDate.grid(row=6,column=0,sticky=W)
        txtExpireDate=Entry(DataFrameLeft,textvariable=self.expDate_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtExpireDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtSideEffect.grid(row=8,column=1)

        #.............Left box but on right hand side............

        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec & Warning:",padx=2,pady=6)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtPrecWarning.grid(row=0,column=3)

        lblDosAge=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=2,pady=6)
        lblDosAge.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=2,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product Qt:",padx=2,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtProductQt.grid(row=3,column=3)

#.................Images on left box..............................

        lblHome=Label(DataFrameLeft,font=("arial",12,"bold"),text="Stay Home Stay Safe:",padx=2,pady=6,bg="white",fg="red")
        lblHome.place(x=430,y=150)

        img1 = Image.open("C:\PHARMA\clients.jpg")
        img1 = img1.resize((130,120), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg,borderwidth=0)
        b1.place(x=605,y=345)

        img2 = Image.open("C:\PHARMA\pills.jpg")
        img2 = img2.resize((130,120), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=500,y=345)

        img3 = Image.open("C:\PHARMA\shalf.jpg")
        img3 = img3.resize((120,120), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=400,y=345)

#.......................DataFrameRight................................
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                 fg="darkgreen",font=("Arial",12,"bold"))
        DataFrameRight.place(x=740,y=5,width=500,height=350)

        img4 = Image.open("C:\PHARMA\doctor.jpg")
        img4 = img4.resize((160,120), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=790,y=160)

        img5 = Image.open("C:\PHARMA\pills.jpg")
        img5 = img5.resize((150,120), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=900,y=160)

        img6 = Image.open("C:\PHARMA\hermometer.jpg")
        img6 = img6.resize((130,120), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=1000,y=160)

        img7 = Image.open("C:\PHARMA\shalf.jpg")
        img7 = img7.resize((130,120), Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(self.root,image=self.photoimg7,borderwidth=0)
        b1.place(x=1120,y=160)

        lblrefno = Label(DataFrameRight, font=("arial",12,"bold"), text="Reference No:")
        lblrefno.place(x=0,y=130)
        txtrefno = Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",15,"bold"),bg="white",bd =2, relief= RIDGE,width=14)
        txtrefno.place(x=135,y=130)

        lblMedicineName = Label(DataFrameRight, font=("arial",12,"bold"), text="Medicine Name:")
        lblMedicineName.place(x=0,y=160)
        txtMedicineName = Entry(DataFrameRight,textvariable=self.Addmed_var,font=("arial",15,"bold"),bg="white",bd =2, relief= RIDGE,width=14)
        txtMedicineName.place(x=135,y=160)
       

        # ...................... Side Frame.................................

        side_frame =Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=200,width=290,height=100)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,columns=("ref","medname"),xscrollcommand=sc_x,yscrollcommand=sc_y)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.xview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)
        
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        #............................Medicine Add Button................

        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=320,y=150,height=160)

        self.btnAddmed = Button(down_frame, text="ADD", font=("arial", 12, "bold"), width=12, bg="lime", fg="white", pady=4, padx=2, command=self.AddMed)
        self.btnAddmed.grid(row=0,column=0)

        self.btnUpdatemed = Button(down_frame,text="Update",command=self.UpdateMed,font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4,padx=2)
        self.btnUpdatemed.grid(row=1,column=0)

        self.btnDeletemed = Button(down_frame,text="Delete",command=self.DeleteMed,font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4,padx=2)
        self.btnDeletemed.grid(row=2,column=0)

        self.btnClearmed = Button(down_frame,text="Clear",command=self.ClearMed,font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4,padx=2)
        self.btnClearmed.grid(row=3,column=0)

        #...................Frame Details........................

        framedetails=Frame(self.root,bd=15,relief=RIDGE)
        framedetails.place(x=0,y=560,width=1365,height=210)

        #...................Table and Scroller....................

        table_frame=Frame(framedetails,bd=15,relief=RIDGE,padx=20)
        table_frame.place(x=0,y=1,width=1300,height=100)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(table_frame,columns=("reg","companyname","type","tabletname","lotno","issuedate",
                                                              "expdate","uses","sideeffect","warning","dosage","price","productQt")
                                                              ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_x.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Expire Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productQt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productQt",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

#....................Add Medicine Functionality..............................

    def AddMed(self):
        print("AddMed method invoked")
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(

                                                                                self.refMed_var.get(),
                                                                                self.Addmed_var.get()
                                                                     ))

        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Successfully","Added Medicine")
        
    #............................fetch and display on table...........................    
    def fetch_dataMed(self):
        
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.medicine_table.delete(*self.medicine_table.get_children())
                for i in rows:
                        self.medicine_table.insert("",END,values=i)
                        
                conn.commit()
        conn.close()
        
        
#...........................Med Get Cursor.................................

    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.Addmed_var.set(row[1])
        
#..........................Update.........................................

    def UpdateMed(self):
        if self.refMed_var.get() =="" or self.Addmed_var.get()=="":
                messagebox.showerror("Error","All fields are required")
        else:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
                my_cursor=conn.cursor()
                my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                                                                                self.Addmed_var.get(),
                                                                                self.refMed_var.get(),
                                                                                
                                                                                 )) 
                conn.commit()
                self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Successfully","Updated Medicine")
        
        
#............................Delete......................................

    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
        my_cursor=conn.cursor()
        
        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)
        
        conn.commit()
        self.fetch_dataMed()
        conn.close()

#.........................Clear...........................................................
    def ClearMed(self):
        self.refMed_var.set("")
        self.Addmed_var.set("")
        
        
#................................Main Table Button Funcionality  Add............................

    def add_data(self):
        if self.ref_var.get() =="" or self.lot_var.get()=="":
                messagebox.showerror("Error","All fields are required")
        else:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into pharmacy_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.ref_var.get(),
                                                                                self.cmpName_var.get(),
                                                                                self.typeMed_var.get(),
                                                                                self.medName_var.get(),
                                                                                self.lot_var.get(),
                                                                                self.issueDate_var.get(),
                                                                                self.expDate_var.get(),
                                                                                self.uses_var.get(),
                                                                                self.sideEffect_var.get(),
                                                                                self.warning_var.get(),
                                                                                self.dosage_var.get(),
                                                                                self.price_var.get(),
                                                                                self.product_var.get()
                                                                                
                                                                                
                                                                                 )) 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successfully","Added Medicine Information")
                
#............................................Update........................

    def fetch_data(self):
            
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy_info")
        row=my_cursor.fetchall()
        if len(row)!=0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in row:
                        self.pharmacy_table .insert("",END,values=i)
                        
                conn.commit()
        conn.close()
        
 #......................................Fetch From Database...........................
     
    def get_cursor(self, event=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        self.ref_var.set(row[0])
        self.cmpName_var.set(row[1])
        self.typeMed_var.set(row[2])
        self.medName_var.set(row[3])
        self.lot_var.set(row[4])
        self.issueDate_var.set(row[5])
        self.expDate_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideEffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.product_var.set(row[12])
        
    #.............................Updat main table ....................................................    
    def update_Med(self):
             if self.ref_var.get() =="" or self.lot_var.get()=="":
                messagebox.showerror("Error","All fields are required")
             else:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
                my_cursor=conn.cursor()
                my_cursor.execute("update pharmacy_info set companyname=%s,type=%s,tabletname=%s,lotno=%s,issuedate=%s,expdate=%s,uses=%s, sideeffect=%s,warning=%s,dosage=%s,price=%s,productQt=%s where ref_no=%s",(
                                                                                                                                                        
                                                                                                                                                        self.cmpName_var.get(),
                                                                                                                                                        self.typeMed_var.get(),
                                                                                                                                                        self.medName_var.get(),
                                                                                                                                                        self.lot_var.get(),
                                                                                                                                                        self.issueDate_var.get(),
                                                                                                                                                        self.expDate_var.get(),
                                                                                                                                                        self.uses_var.get(),
                                                                                                                                                        self.sideEffect_var.get(),
                                                                                                                                                        self.warning_var.get(),
                                                                                                                                                        self.dosage_var.get(),
                                                                                                                                                        self.price_var.get(),
                                                                                                                                                        self.product_var.get(),
                                                                                                                                                        self.ref_var.get(),
                                                                                                                                                        
                                                                                                                                                        )) 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successfully","Updated Medicine")
            
        
#............................Delete from main table......................................

    def deleteMed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
        my_cursor=conn.cursor()
        
        sql="delete from pharmacy_info where ref_no=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)
        
        conn.commit()
        self.fetch_data()
        conn.close()
        
        messagebox.showinfo("Deleted","Information deleted successfully") 

#............................Reset Function...........................................
    def reset(self):
        
        self.cmpName_var.set(""),
        self.lot_var.set(""),
        self.issueDate_var.set(""),
        self.expDate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(""),
        self.price_var.set(""),
        self.product_var.set("")
        
#....................................Search........................................................
    def search_data(self):  
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="pharmacydb")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy_info WHERE `" + str(self.search_var.get()) + "` LIKE '%" + str(self.searchTxt_var.get()) + "%'")

        row=my_cursor.fetchall()
        if len(row)!=0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in row:
                        self.pharmacy_table.insert("",END,values=i)
                conn.commit()
        conn.close()

if __name__ == "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()

        
        
if __name__=="__main__":
    main()