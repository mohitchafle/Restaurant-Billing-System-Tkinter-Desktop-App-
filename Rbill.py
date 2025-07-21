
from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Restaurent Billing System by - MoHiT")
        title=Label(self.root,text="Restaurent Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#d84315",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.Lemon_tea=IntVar()
        self.Mango_Tea=IntVar()
        self.Green_tea=IntVar()
        self.Mint_tea=IntVar()
        self.Espresso=IntVar()
        self.Americano=IntVar()
        self.Black_Coffee=IntVar()
        self.Orange_Juice=IntVar()
        self.Apple_Juice=IntVar()
        self.Pineapple_Juice=IntVar()
        self.Grape_Juice=IntVar()
        self.Lemon_Juice=IntVar()
        self.Cherry_Juice=IntVar()
        self.Blueberry_Juice=IntVar()
        self.Noodles=IntVar()
        self.aloo=IntVar()
        self.Dahi_vada=IntVar()
        self.Pav_Bhaji=IntVar()
        self.Bhel_Puri=IntVar()
        self.Samosa=IntVar()
        self.Dabeli=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(10,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        
        
        #customer details 
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#d84315",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#d84315",fg="white").grid(row=0,column=0,padx=15)

        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#d84315",fg="white").grid(row=0,column=2,padx=10)

        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#d84315",fg="white").grid(row=0,column=4,padx=10)

        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        
        #Resturant Menu
        # Tea/Coffee
        snacks=LabelFrame(self.root,text="Tea / Coffee",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        snacks.place(x=5,y=180,height=380,width=325)

        item1=Label(snacks,text="Lemon Tea",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Lemon_tea).grid(row=0,column=1,padx=10)

        item2=Label(snacks,text="Mango Tea",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Mango_Tea).grid(row=1,column=1,padx=10)

        item3=Label(snacks,text="Green Tea",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Green_tea).grid(row=2,column=1,padx=10)

        item4=Label(snacks,text="Mint Tea",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Mint_tea).grid(row=3,column=1,padx=10)

        item5=Label(snacks,text="Espresso",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Espresso).grid(row=4,column=1,padx=10)

        item6=Label(snacks,text="Americano",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Americano).grid(row=5,column=1,padx=10)

        item7=Label(snacks,text="Black Coffee",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Black_Coffee).grid(row=6,column=1,padx=10)
        
        # Fruit Juices
        grocery=LabelFrame(self.root,text="Juices",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        grocery.place(x=340,y=180,height=380,width=325)

        item8=Label(grocery,text="Orange Juice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Orange_Juice).grid(row=0,column=1,padx=10)

        item9=Label(grocery,text="Apple Juice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Apple_Juice).grid(row=1,column=1,padx=10)

        item10=Label(grocery,text="Pineapple Juice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Pineapple_Juice).grid(row=2,column=1,padx=10)

        item11=Label(grocery,text="Grape Juice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Grape_Juice).grid(row=3,column=1,padx=10)

        item12=Label(grocery,text="Lemon Juice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Lemon_Juice).grid(row=4,column=1,padx=10)

        item13=Label(grocery,text="Cherry Juice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Cherry_Juice).grid(row=5,column=1,padx=10)

        item14=Label(grocery,text="Blueberry Juice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Blueberry_Juice).grid(row=6,column=1,padx=10)
        
        #Snacks
        hygine=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        hygine.place(x=677,y=180,height=380,width=325)

        item15=Label(hygine,text="Noodles",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Noodles).grid(row=0,column=1,padx=10)

        item16=Label(hygine,text="Aloo Tikki Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.aloo).grid(row=1,column=1,padx=10)

        item17=Label(hygine,text="Dahi Vada",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Dahi_vada).grid(row=2,column=1,padx=10)

        item18=Label(hygine,text="Pav Bhaji",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Pav_Bhaji).grid(row=3,column=1,padx=10)

        item19=Label(hygine,text="Bhel Puri",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Bhel_Puri).grid(row=4,column=1,padx=10)

        item20=Label(hygine,text="Samosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Samosa).grid(row=5,column=1,padx=10)

        item21=Label(hygine,text="Dabeli",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Dabeli).grid(row=6,column=1,padx=10)
        
        #billarea
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372) 

        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#d84315",fg="White").pack(fill=X)

        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #billing menu
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)

        total_snacks=Label(billing_menu,text="Total Beverages Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)

        total_grocery=Label(billing_menu,text="Total Juices Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=7)


        total_hygine=Label(billing_menu,text="Total Snacks Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=7)

        tax_snacks=Label(billing_menu,text="Beverage Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)

        tax_grocery=Label(billing_menu,text="Juice Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)


        tax_hygine=Label(billing_menu,text="Snack Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=2)
        tax_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)

        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#d84315",fg="white",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#d84315",fg="white",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#d84315",fg="white",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        button_save = Button(button_frame, text="Save Bill", font=("Arial Black", 15), pady=10, bg="#d84315", fg="white", command=lambda: save_bill(self))
        button_save.grid(row=0, column=3, padx=10, pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu=self.Lemon_tea.get()*29
    self.no=self.Mango_Tea.get()*39
    self.la=self.Green_tea.get()*39
    self.ore=self.Mint_tea.get()*49
    self.mu=self.Espresso.get()*119
    self.si=self.Americano.get()*119
    self.na=self.Black_Coffee.get()*25
    total_snacks_price=(
                self.nu+
                self.no+
                self.la+
                self.ore+
                self.mu+
                self.si+
                self.na)
    self.total_sna.set(str(total_snacks_price)+" Rs")
    self.a.set(str(round(total_snacks_price*0.05,3))+" Rs")

    self.at=self.Orange_Juice.get()*49
    self.pa=self.Apple_Juice.get()*49
    self.oi=self.Grape_Juice.get()*49
    self.ri=self.Pineapple_Juice.get()*49
    self.su=self.Lemon_Juice.get()*49
    self.te=self.Blueberry_Juice.get()*89
    self.da=self.Cherry_Juice.get()*89
    total_grocery_price=(
        self.at+
        self.pa+
        self.oi+
        self.ri+
        self.su+
        self.te+
        self.da)

    self.total_gro.set(str(total_grocery_price)+" Rs")
    self.b.set(str(round(total_grocery_price*0.01,3))+" Rs")

    self.so=self.Noodles.get()*89
    self.sh=self.aloo.get()*49
    self.cr=self.Pav_Bhaji.get()*49
    self.lo=self.Dahi_vada.get()*49
    self.fo=self.Bhel_Puri.get()*49
    self.ma=self.Samosa.get()*30
    self.sa=self.Dabeli.get()*49

    total_hygine_price=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)

    self.total_hyg.set(str(total_hygine_price)+" Rs")
    self.c.set(str(round(total_hygine_price*0.10,3))+" Rs")
    self.total_all_bill=(total_snacks_price+
                total_grocery_price+
                total_hygine_price+
                (round(total_grocery_price*0.01,3))+
                (round(total_hygine_price*0.10,3))+
                (round(total_snacks_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO OUR RESTAURANT\n\t    Phone-No.93715XXX3")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.Lemon_tea.get()!=0:
        self.txtarea.insert(END,f"Lemon Tea\t\t {self.Lemon_tea.get()}\t{self.nu}\n")
    if self.Mango_Tea.get()!=0:
        self.txtarea.insert(END,f"Mango Tea\t\t {self.Mango_Tea.get()}\t{self.no}\n")
    if self.Green_tea.get()!=0:
        self.txtarea.insert(END,f"Green Tea\t\t {self.Green_tea.get()}\t{self.la}\n")
    if self.Mint_tea.get()!=0:
        self.txtarea.insert(END,f"Mint Tea\t\t {self.Mint_tea.get()}\t{self.ore}\n")
    if self.Espresso.get()!=0:
        self.txtarea.insert(END,f"Espresso\t\t {self.Espresso.get()}\t{self.mu}\n")
    if self.Americano.get()!=0:
        self.txtarea.insert(END,f"Americano\t\t {self.Americano.get()}\t{self.si}\n")
    if self.Black_Coffee.get()!=0:
        self.txtarea.insert(END,f"Black Coffee\t\t {self.Black_Coffee.get()}\t{self.na}\n")
    if self.Orange_Juice.get()!=0:
        self.txtarea.insert(END,f"Orange Juice\t\t {self.Orange_Juice.get()}\t{self.at}\n")
    if self.Apple_Juice.get()!=0:
        self.txtarea.insert(END,f"Apple Juice\t\t {self.Apple_Juice.get()}\t{self.pa}\n")
    if self.Pineapple_Juice.get()!=0:
        self.txtarea.insert(END,f"Pineapple Juice\t\t {self.Pineapple_Juice.get()}\t{self.ri}\n")
    if self.Grape_Juice.get()!=0:
        self.txtarea.insert(END,f"Grape Juice\t\t {self.Grape_Juice.get()}\t{self.oi}\n")
    if self.Lemon_Juice.get()!=0:
        self.txtarea.insert(END,f"Lemon Juice\t\t {self.Lemon_Juice.get()}\t{self.su}\n")
    if self.Cherry_Juice.get()!=0:
        self.txtarea.insert(END,f"Cherry_Juice\t\t {self.Cherry_Juice.get()}\t{self.da}\n")
    if self.Blueberry_Juice.get()!=0:
        self.txtarea.insert(END,f"Blueberry Juice\t\t {self.Blueberry_Juice.get()}\t{self.te}\n")
    if self.Noodles.get()!=0:
        self.txtarea.insert(END,f"Noodles\t\t {self.Noodles.get()}\t{self.so}\n")
    if self.aloo.get()!=0:
        self.txtarea.insert(END,f"Aloo Tikki Chaat\t\t {self.aloo.get()}\t{self.sh}\n")
    if self.Dahi_vada.get()!=0:
        self.txtarea.insert(END,f"Dahi Vada\t\t {self.Dahi_vada.get()}\t{self.lo}\n")
    if self.Pav_Bhaji.get()!=0:
        self.txtarea.insert(END,f"Pav Bhaji\t\t {self.Pav_Bhaji.get()}\t{self.cr}\n")
    if self.Bhel_Puri.get()!=0:
        self.txtarea.insert(END,f"Bhel_Puri\t\t {self.Bhel_Puri.get()}\t{self.fo}\n")
    if self.Samosa.get()!=0:
        self.txtarea.insert(END,f"Samosa\t\t {self.Samosa.get()}\t{self.ma}\n")
    if self.Dabeli.get()!=0:
        self.txtarea.insert(END,f"Dabeli\t\t {self.Dabeli.get()}\t{self.sa}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Beverage Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Juice Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.c.get()}\n \n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.Lemon_tea.set(0)
        self.Mango_Tea.set(0)
        self.Green_tea.set(0)
        self.Mint_tea.set(0)
        self.Espresso.set(0)
        self.Americano.set(0)
        self.Black_Coffee.set(0)
        self.Orange_Juice.set(0)
        self.Apple_Juice.set(0)
        self.Pineapple_Juice.set(0)
        self.Grape_Juice.set(0)
        self.Lemon_Juice.set(0)
        self.Cherry_Juice.set(0)
        self.Blueberry_Juice.set(0)
        self.Noodles.set(0)
        self.aloo.set(0)
        self.Dahi_vada.set(0)
        self.Pav_Bhaji.set(0)
        self.Bhel_Puri.set(0)
        self.Samosa.set(0)
        self.Dabeli.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

def save_bill(self):
    if self.txtarea.get('1.0', END).strip():  # Check if bill area is not empty
        bill_content = self.txtarea.get('1.0', END)
        file_name = f"Bill_{self.bill_no.get()}.txt"
        try:
            with open(file_name, "w") as f:
                f.write(bill_content)
            messagebox.showinfo("Success", f"Bill saved successfully as {file_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save bill: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Bill area is empty! Generate the bill first.")

# Add a button to trigger the save_bill function

    

root=Tk()
obj=Bill_App(root)
root.mainloop()