from tkinter import *
import random
import os
import sys
from tkinter import messagebox
import pymysql as py


class Bill_App:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="cyan")
        self.root.title("Billing System")
        title=Label(self.root,text="Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="red",fg="Blue").pack(fill=X)

        #===================================variables=======================================================================================
        self.ChikkenBiriyani=IntVar()
        self.MuttonBiriyani=IntVar()
        self.Chikkenrice=IntVar()
        self.PrawnBiriyani=IntVar()
        self.chikken65fry=IntVar()
        self.MuttonGravy=IntVar()
        self.chikkenGravy=IntVar()
        self.Idly=IntVar()
        self.Dosa=IntVar()
        self.poori=IntVar()
        self.GobiManchurian=IntVar()
        self.parotta=IntVar()
        self.MasalaDosa=IntVar()
        self.paneerGravy=IntVar()
        self.total_Non_veg=StringVar()
        self.total_Veg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="red",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="red",fg="white").grid(row=0,column=0,padx=15)
        
        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)
        
        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="red",fg="white").grid(row=0,column=2,padx=10)
        
        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)
        
        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="red",fg="white").grid(row=0,column=4,padx=10)
        
        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Non-veg frame=================================================================
        Non_veg=LabelFrame(self.root,text="Non_veg",font=("Arial Black",12),bg="red",fg="white",relief=GROOVE,bd=10)
        Non_veg.place(x=5,y=180,height=380,width=325)
        
        item1=Label(Non_veg,text="ChikkenBiriyani",font=("Arial Black",11),bg="red",fg="white").grid(row=0,column=0,pady=11)
        item1_entry=Entry(Non_veg,borderwidth=2,width=15,textvariable=self.ChikkenBiriyani).grid(row=0,column=1,padx=10)

        item2=Label(Non_veg,text="MuttonBiriyani",font=("Arial Black",11),bg="red",fg="white").grid(row=1,column=0,pady=11)
        item2_entry=Entry(Non_veg,borderwidth=2,width=15,textvariable=self.MuttonBiriyani).grid(row=1,column=1,padx=10)

        item3=Label(Non_veg,text="Chikkenrice",font=("Arial Black",11),bg="red",fg="white").grid(row=2,column=0,pady=11)
        item3_entry=Entry(Non_veg,borderwidth=2,width=15,textvariable=self.Chikkenrice).grid(row=2,column=1,padx=10)

        item4=Label(Non_veg,text="PrawnBiriyani",font=("Arial Black",11),bg="red",fg="white").grid(row=3,column=0,pady=11)
        item4_entry=Entry(Non_veg,borderwidth=2,width=15,textvariable=self.PrawnBiriyani).grid(row=3,column=1,padx=10)

        item5=Label(Non_veg,text="chikken65fry",font=("Arial Black",11),bg="red",fg="white").grid(row=4,column=0,pady=11)
        item5_entry=Entry(Non_veg,borderwidth=2,width=15,textvariable=self.chikken65fry).grid(row=4,column=1,padx=10)

        item6=Label(Non_veg,text="MuttonGravy",font=("Arial Black",11),bg="red",fg="white").grid(row=5,column=0,pady=11)
        item6_entry=Entry(Non_veg,borderwidth=2,width=15,textvariable=self.MuttonGravy).grid(row=5,column=1,padx=10)

        item7=Label(Non_veg,text="chikkenGravy",font=("Arial Black",11),bg="red",fg="white").grid(row=6,column=0,pady=11)
        item7_entry=Entry(Non_veg,borderwidth=2,width=15,textvariable=self.chikkenGravy).grid(row=6,column=1,padx=10)
        #===================================Veg=====================================================================================
        Veg=LabelFrame(self.root,text="Veg",font=("Arial Black",12),relief=GROOVE,bd=10,bg="red",fg="white")
        Veg.place(x=340,y=180,height=380,width=325)

        item8=Label(Veg,text="Idly",font=("Arial Black",11),bg="red",fg="white").grid(row=0,column=0,pady=11)
        item8_entry=Entry(Veg,borderwidth=2,width=15,textvariable=self.Idly).grid(row=0,column=1,padx=10)

        item9=Label(Veg,text="Dosa",font=("Arial Black",11),bg="red",fg="white").grid(row=1,column=0,pady=11)
        item9_entry=Entry(Veg,borderwidth=2,width=15,textvariable=self.Dosa).grid(row=1,column=1,padx=10)

        item10=Label(Veg,text="poori",font=("Arial Black",11),bg="red",fg="white").grid(row=2,column=0,pady=11)
        item10_entry=Entry(Veg,borderwidth=2,width=15,textvariable=self.poori).grid(row=2,column=1,padx=10)

        item11=Label(Veg,text="GobiManchurian",font=("Arial Black",11),bg="red",fg="white").grid(row=3,column=0,pady=11)
        item11_entry=Entry(Veg,borderwidth=2,width=15,textvariable=self.GobiManchurian).grid(row=3,column=1,padx=10)

        item12=Label(Veg,text="parotta",font=("Arial Black",11),bg="red",fg="white").grid(row=4,column=0,pady=11)
        item12_entry=Entry(Veg,borderwidth=2,width=15,textvariable=self.parotta).grid(row=4,column=1,padx=10)

        item13=Label(Veg,text="MasalaDosa",font=("Arial Black",11),bg="red",fg="white").grid(row=5,column=0,pady=11)
        item13_entry=Entry(Veg,borderwidth=2,width=15,textvariable=self.MasalaDosa).grid(row=5,column=1,padx=10)

        item14=Label(Veg,text="paneerGravy",font=("Arial Black",11),bg="red",fg="white").grid(row=6,column=0,pady=11)
        item14_entry=Entry(Veg,borderwidth=2,width=15,textvariable=self.paneerGravy).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="red")
        billarea.place(x=1010,y=188,width=330,height=372)
        
        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="red",fg="white").pack(fill=X)
        
        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="red",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)
        
        total_Non_veg=Label(billing_menu,text="Total Non_veg Price",font=("Arial Black",11),bg="red",fg="white").grid(row=0,column=0)
        total_Non_veg_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_Non_veg).grid(row=0,column=1,padx=10,pady=7)
        
        total_Veg=Label(billing_menu,text="Total Veg Price",font=("Arial Black",11),bg="red",fg="white").grid(row=1,column=0)
        total_Veg_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_Veg).grid(row=1,column=1,padx=10,pady=7)

        tax_Non_veg=Label(billing_menu,text="Non_veg Tax",font=("Arial Black",11),bg="red",fg="white").grid(row=0,column=2)
        tax_Non_veg_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)
        
        tax_Veg=Label(billing_menu,text="Veg Tax",font=("Arial Black",11),bg="red",fg="white").grid(row=1,column=2)
        tax_Veg_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)

        
        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="white")
        button_frame.place(x=830,width=500,height=95)

        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="red",fg="white",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_save=Button(button_frame,text="Save",font=("Arial Black",15),pady=10,bg="red",fg="white",command=lambda:save(self)).grid(row=0,column=1,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="red",fg="white",command=lambda:clear(self)).grid(row=0,column=2,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",14),pady=10,bg="red",fg="white",width=8,command=lambda:exit1(self)).grid(row=0,column=3,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.CB=self.ChikkenBiriyani.get()*150
    self.MB=self.MuttonBiriyani.get()*200
    self.CR=self.Chikkenrice.get()*100
    self.PB=self.PrawnBiriyani.get()*150
    self.C65=self.chikken65fry.get()*100
    self.MG=self.MuttonGravy.get()*130
    self.CG=self.chikkenGravy.get()*100
    total_Non_veg_price=(
                self.CB+
                self.MB+
                self.CR+
                self.PB+
                self.C65+
                self.MG+
                self.CG)          
    self.total_Non_veg.set(str(total_Non_veg_price)+" Rs")
    self.a.set(str(round(total_Non_veg_price*0.05,3))+" Rs")

    self.id=self.Idly.get()*30
    self.Do=self.Dosa.get()*30
    self.po=self.poori.get()*30
    self.GM=self.GobiManchurian.get()*60
    self.PA=self.parotta.get()*40
    self.MD=self.MasalaDosa.get()*40
    self.PG=self.paneerGravy.get()*100
    total_Veg_price=(
        self.id+
        self.Do+
        self.po+
        self.GM+
        self.PA+
        self.MD+
        self.PG)
        
    self.total_Veg.set(str(total_Veg_price)+" Rs")
    self.b.set(str(round(total_Veg_price*0.01,3))+" Rs")
    self.total_all_bill=(total_Non_veg_price+
                total_Veg_price+
                (round(total_Veg_price*0.01,3))+
                (round(total_Non_veg_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
    
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,f"\tGN Restaurant \n\tPhone-No.9791086295")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")

def save(self):
    op=messagebox.askyesno("Save","Do you want to save the Bill")
    if op>0:
        self.bill_data=self.txtarea.get(1.0,END)
        f1=open("rest bill.txt",'w+')
        f1.write(self.bill_data)
        op1=messagebox.showinfo("Saved",f"Bill no:{self.bill_no.get()} Saved Successfully")
        f1.close()

        e_name =self.c_name.get()
        e_Qnty = self.phone.get()
        e_price = self.bill_no.get()

        conn = py.connect(host="localhost",user="root", password="",  database="restaurant")
        cur = conn.cursor()
        cur.execute("insert into details(name, phone,billno) values('"+e_name+"', '"+e_Qnty+"', '"+e_price+"')")
        cur.fetchall()
        messagebox.showinfo('info','data inserted',parent = self.root)
        conn.close()


def billarea(self):
    
    intro(self)
    if self.ChikkenBiriyani.get()!=0:
        self.txtarea.insert(END,f"ChikkenBiriyani\t\t {self.ChikkenBiriyani.get()}\t{self.CB}\n")
    if self.MuttonBiriyani.get()!=0:
        self.txtarea.insert(END,f"MuttonBiriyani\t\t {self.MuttonBiriyani.get()}\t{self.MB}\n")
    if self.Chikkenrice.get()!=0:
        self.txtarea.insert(END,f"Chikkenrice\t\t {self.Chikkenrice.get()}\t{self.CR}\n")
    if self.PrawnBiriyani.get()!=0:
        self.txtarea.insert(END,f"PrawnBiriyani\t\t {self.PrawnBiriyani.get()}\t{self.PB}\n")
    if self.chikken65fry.get()!=0:
        self.txtarea.insert(END,f"chikken65fry\t\t {self.chikken65fry.get()}\t{self.C65}\n")
    if self.MuttonGravy.get()!=0:
        self.txtarea.insert(END,f"MuttonGravy\t\t {self.MuttonGravy.get()}\t{self.MG}\n")
    if self.chikkenGravy.get()!=0:
        self.txtarea.insert(END,f"chikkenGravy\t\t {self.chikkenGravy.get()}\t{self.CG}\n")
    if self.Idly.get()!=0:
        self.txtarea.insert(END,f"Idly\t\t {self.Idly.get()}\t{self.id}\n")
    if self.Dosa.get()!=0:
        self.txtarea.insert(END,f"Dosa\t\t {self.Dosa.get()}\t{self.Do}\n")
    if self.poori.get()!=0:
        self.txtarea.insert(END,f"poori\t\t {self.poori.get()}\t{self.po}\n")
    if self.GobiManchurian.get()!=0:
        self.txtarea.insert(END,f"GobiManchurian\t\t {self.GobiManchurian.get()}\t{self.GM}\n")
    if self.parotta.get()!=0:
        self.txtarea.insert(END,f"parotta\t\t {self.parotta.get()}\t{self.PA}\n")
    if self.MasalaDosa.get()!=0:
        self.txtarea.insert(END,f"MasalaDosa\t\t {self.MasalaDosa.get()}\t{self.MD}\n")
    if self.paneerGravy.get()!=0:
        self.txtarea.insert(END,f"paneerGravy\t\t {self.paneerGravy.get()}\t{self.PG}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Non_veg Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Veg Tax : {self.b.get()}\n")

    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.ChikkenBiriyani.set(0)
        self.MuttonBiriyani.set(0)
        self.Chikkenrice.set(0)
        self.PrawnBiriyani.set(0)
        self.chikken65fry.set(0)
        self.MuttonGravy.set(0)
        self.chikkenGravy.set(0)
        self.Idly.set(0)
        self.Dosa.set(0)
        self.poori.set(0)
        self.GobiManchurian.set(0)
        self.parotta.set(0)
        self.MasalaDosa.set(0)
        self.paneerGravy.set(0)
        self.total_Non_veg.set(0)
        self.total_Veg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

if __name__=="__main__":
    
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
    
