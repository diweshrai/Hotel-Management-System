from tkinter import*
from tkinter.font import BOLD

from PIL import Image,ImageTk 

from tkinter import ttk

import mysql.connector

import random

from tkinter import messagebox

from mysql.connector import cursor

from time import strptime

from time import strftime

from datetime import datetime



class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")



        #variables

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()




        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)




#logo

        img2=Image.open(r"H:\WhatsApp\room1.jpg")
        img2=img2.resize((600,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

       # lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        #lbling.place(x=0,y=0,width=300,height=300)



#label frame roombooking

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING DETAILS" ,padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=455,height=480)    

#labels and entry


#romm details entruy

        lbl_cust_contact=Label(labelframeleft,text="Customer conatact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20 ,font=("times new roman",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)


       #fetch data button
        
        btnFetchData=Button(labelframeleft,text="FetchData",command=self.Fetch_contact,font=("arial",13,"bold"),width=8,bg="black",fg="gold")
        btnFetchData.place(x=350,y=4)

#cust check in date


        check_in_date=Label(labelframeleft,text="check-in-date",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)


#check out date


        lbl_check_out=Label(labelframeleft,text="check-out-date",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)

        txtlbl_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txtlbl_check_out.grid(row=2,column=1)



        #room type


        label_Roomtype=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        label_Roomtype.grid(row=3,column=0,sticky=W)

       # conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
        #my_cursor=conn.cursor()
        #my_cursor.execute("select RoomType from details")
        #rooww=my_cursor.fetchall()
       

        combo_Roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Roomtype["value"]=("Single","Double","luxury")
        combo_Roomtype.grid(row=3,column=1)
        combo_Roomtype.current(0)


        #Avaliable room


        lblRoomAvailable=Label(labelframeleft,text="Room Available",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
       


        combo_roomno=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_roomno["value"]=rows
        combo_roomno.grid(row=4,column=1)
        combo_roomno.current(0)

        #txtlblRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        #txtlblRoomAvailable.grid(row=4,column=1)

# meal
        lblMeal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)


        combo_Meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Meal["value"]=("BreakFast","Lunch","Dinner")
        combo_Meal.grid(row=5,column=1)
        combo_Meal.current(0)
        
        #txtlblMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        #txtlblMeal.grid(row=5,column=1)

  #no of days
        
        lblNoofDays=Label(labelframeleft,text="No-of-Days",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=6,column=0,sticky=W)

        txtlblNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txtlblNoofDays.grid(row=6,column=1)

      # paid tax
       
      
        lblNoofDays=Label(labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=7,column=0,sticky=W)

        txtlblNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"),state="readonly")
        txtlblNoofDays.grid(row=7,column=1)


        #sub total


        
        lblNoofDays=Label(labelframeleft,text="Sub-Total",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=8,column=0,sticky=W)

        txtlblNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"),state="readonly")
        txtlblNoofDays.grid(row=8,column=1)




        #total cost


        lblidnumber=Label(labelframeleft,text="Total-cost",font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)

        txtlblidnumber=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"),state="readonly")
        txtlblidnumber.grid(row=9,column=1)
        

# bill button


        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

# BUTTONS


        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=440,height=40)


        #add button
        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btnadd.grid(row=0,column=0)



        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btnupdate.grid(row=0,column=1)

        

        btndelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btndelete.grid(row=0,column=2)


        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btnreset.grid(row=0,column=3)

        img3=Image.open(r"H:\WhatsApp\2.png")
        img3=img3.resize((520,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=760,y=55,width=520,height=200)

#table frame search


        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search Sysytem" ,padx=2,font=("times new roman",12,"bold"))
        Table_frame.place(x=470,y=280,width=835,height=480)    
        
        searchby=Label(Table_frame,text="SEARCH BY",font=("arial",12,"bold"),bg="red",fg="white")
        searchby.grid(row=0,column=0,sticky=W)
        
        self.serch_var=StringVar()
        combo_search=ttk.Combobox(Table_frame,font=("arial",12,"bold"),width=12,state="readonly",textvariable=self.serch_var)
        combo_search["value"]=("contact")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)


        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=20)
        txtsearch.grid(row=0,column=2,padx=2)


        btnsearch=Button(Table_frame,text="SEARCH",command=self.search,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btnsearch.grid(row=0,column=3,padx=5)


        btnshowall=Button(Table_frame,text="SHOW ALL",command=self.fetch_data,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btnshowall.grid(row=0,column=4,padx=5)



 #show data table



        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=820,height=180)
       

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
       
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
       
        scroll_y.config(command=self.room_table.yview) 


        self.room_table.heading("contact",text="contact")
        self.room_table.heading("checkin",text="check-in-Date")
        self.room_table.heading("checkout",text="check-out-Date")
        self.room_table.heading("roomtype",text="Room-Type")
        self.room_table.heading("roomavailable",text="RoomAvailable")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No-Of-Days")
        

        self.room_table["show"]="headings"


        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)    
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)


        self.room_table.pack(fill=BOTH,expand=1)

        self.fetch_data()
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)



# fetch data functionality



    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter contact no",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
            my_cursor=conn.cursor()
            query=("select Name from custo where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("error","this contact no not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=465,y=60,width=280,height=200) 

                lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0) 

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)  



#gender fetching

                conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from custo where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30) 

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=30)  
 
# email fetching


                
                conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
                my_cursor=conn.cursor()
                query=("select Email from custo where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=60) 

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=60) 



        #nationaliy fetching

                conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
                my_cursor=conn.cursor()
                query=("select nationality from custo where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=90) 

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=90) 
 




 #address fetching


                conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
                my_cursor=conn.cursor()
                query=("select address from custo where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="ADDRESS:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=120) 

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120) 
  
                 
                 


# insertinng data into database


    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
                messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:
               
               conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into room values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                           self.var_contact.get(),
                                                                           self.var_checkin.get(),
                                                                           self.var_checkout.get(),
                                                                           self.var_roomtype.get(),
                                                                           self.var_roomavailable.get(),
                                                                           self.var_meal.get(),
                                                                           self.var_noofdays.get(),
                                                                            






                                                                        )) 
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("success","Room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)


     #fetch data                                                                          

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:        
                self.room_table.insert("",END,values=i)

            conn.commit()
            conn.close()



    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]


        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6]),



        #update button functionality



    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter contact number",parent=self.root)
        else:                
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
                                  
                                  
            
                                                                                                                                                                
                                                                                                                                                                 
                                                                           self.var_checkin.get(),
                                                                           self.var_checkout.get(),
                                                                           self.var_roomtype.get(),
                                                                           self.var_roomavailable.get(),
                                                                           self.var_meal.get(),
                                                                           self.var_noofdays.get(),
                                                                           self.var_contact.get()        )) 
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","data updates succesfully")
   
                         
#delete button functionality


    def mdelete(self):
        mdelete=messagebox.askyesno("HTM","do you want to delete this",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data
        conn.close()   




         #button reset functionality
                                                        
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set(""),



    
       # inDate=self.var_checkin.get()
        #outDate=self.var_checkout.get()
        #inDate=datetime.strptime(inDate,"%d/%m/%y")
        #outDate=datetime.strptime(outDate,"%d/%m/%y")
        #result=outDate-inDate
        
        #self.var_noofdays.set([result])


    def total(self):
        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(350)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(450)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)



            
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(650)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)



            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(450)
            q2=float(650)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)



            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(650)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)



            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)



            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="luxury"):
            q1=float(450)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)



            
        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)




#search system


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from room where" +str(self.serch_var.get())+'"LIKE%"+str(self.txt_search.get())+"%"')
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()                                    




if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()