from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter import Button


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

        btnUpdatemed = Button(button_frame,text="Login",font=("arial",15,"bold"),width=16,bg="purple",fg="white",pady=4,padx=2)
        btnUpdatemed.grid(row=0,column=3)

        btnDeletemed = Button(button_frame,text="Clear",font=("arial",15,"bold"),width=13,bg="red",fg="white",pady=4,padx=2,command=self.clear)
        btnDeletemed.grid(row=0,column=5)
#.................................Button Functionality...............................
    def register(self):
        print("AddMed method invoked")
        if self.password_var.get() =="" or self.confpassword_var.get()== "":
                messagebox.showerror("Error","All fields are required")
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
        self.confpassword_var.set("")
        

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
        