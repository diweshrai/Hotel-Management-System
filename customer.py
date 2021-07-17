from tkinter import*
from tkinter.font import BOLD

from PIL import Image,ImageTk 

from tkinter import ttk

import mysql.connector

import random

from tkinter import messagebox

from mysql.connector import cursor

class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")



        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

# variables


        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        
        self.var_address=StringVar()






#logo

        img2=Image.open(r"H:\WhatsApp\2.png")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=100,height=50)



#label frame customer

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details" ,padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=455,height=480)    


#labels and entry


#customer ref

        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ref ,font=("times new roman",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

#cust name


        cname=Label(labelframeleft,text="Customer name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_name,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)


#mother name


        lblmname=Label(labelframeleft,text="Mother name",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtlblmname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mother,font=("arial",13,"bold"))
        txtlblmname.grid(row=2,column=1)



        #cust gender combobox


        label_gender=Label(labelframeleft,text="Customer Gender",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Others")
        combo_gender.grid(row=3,column=1)


        #cust post code


        lblpostcode=Label(labelframeleft,text="Customer Post-code",font=("arial",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)

        txtlblpostcode=ttk.Entry(labelframeleft,width=29,textvariable=self.var_post,font=("arial",13,"bold"))
        txtlblpostcode.grid(row=4,column=1)



#cust mobile no


        lblmobile=Label(labelframeleft,text="Mobile no",font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)

        txtlblmobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("arial",13,"bold"))
        txtlblmobile.grid(row=5,column=1)


        #cust email


        lblemail=Label(labelframeleft,text="Customer email",font=("arial",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)

        txtlblemail=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("arial",13,"bold"))
        txtlblemail.grid(row=6,column=1)


#cust nationality


        lblnation=Label(labelframeleft,text="Customer nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblnation.grid(row=7,column=0,sticky=W)

        combo_nation=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nation["value"]=("INDIAN","PAK","Others")
        combo_nation.grid(row=7,column=1)




#cust id proff combobox

        lblproof=Label(labelframeleft,text="Customer ID-Proof",font=("arial",12,"bold"),padx=2,pady=6)
        lblproof.grid(row=8,column=0,sticky=W)

        combo_proof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_proof["value"]=("ADHAR-CARD","PAN-CARD","D-C")
        combo_proof.grid(row=8,column=1)




#cust id number


        lblidnumber=Label(labelframeleft,text="Customer ID-number",font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)

        txtlblidnumber=ttk.Entry(labelframeleft,width=29,textvariable=self.var_idnumber,font=("arial",13,"bold"))
        txtlblidnumber.grid(row=9,column=1)



#cust address


        lbladdress=Label(labelframeleft,text="Customer Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)

        txtlbladdress=ttk.Entry(labelframeleft,width=29,textvariable=self.var_address,font=("arial",13,"bold"))
        txtlbladdress.grid(row=10,column=1)


# BUTTONS


        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=440,height=40)


        #add button
        btnadd=Button(btn_frame,text="ADD",font=("arial",13,"bold"),width=10,bg="black",fg="gold",command=self.add_data)
        btnadd.grid(row=0,column=0)



        btnupdate=Button(btn_frame,text="UPDATE",font=("arial",13,"bold"),width=10,bg="black",fg="gold",command=self.update)
        btnupdate.grid(row=0,column=1)

        

        btndelete=Button(btn_frame,text="DELETE",font=("arial",13,"bold"),width=10,bg="black",fg="gold",command=self.mdelete)
        btndelete.grid(row=0,column=2)


        btnreset=Button(btn_frame,text="RESET",font=("arial",13,"bold"),width=10,bg="black",fg="gold",command=self.reset)
        btnreset.grid(row=0,column=3)



#table frame


        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search Sysytem" ,padx=2,font=("times new roman",12,"bold"))
        Table_frame.place(x=470,y=50,width=835,height=480)    
        
        searchby=Label(Table_frame,text="SEARCH BY",font=("arial",12,"bold"),bg="red",fg="white")
        searchby.grid(row=0,column=0,sticky=W)
        
        self.serch_var=StringVar()
        combo_search=ttk.Combobox(Table_frame,font=("arial",12,"bold"),width=12,state="readonly",textvariable=self.serch_var)
        combo_search["value"]=("ref","mobile")
        combo_search.grid(row=0,column=1,padx=5)


        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=20)
        txtsearch.grid(row=0,column=2,padx=2)


        btnsearch=Button(Table_frame,text="SEARCH",font=("arial",13,"bold"),width=10,bg="black",fg="gold",command=self.search)
        btnsearch.grid(row=0,column=3,padx=5)


        btnshowall=Button(Table_frame,text="SHOW ALL",font=("arial",13,"bold"),width=10,bg="black",fg="gold",command=self.fetch_data)
        btnshowall.grid(row=0,column=4,padx=5)





        #show data table



        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=820,height=395)
       

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
       
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
       
        scroll_y.config(command=self.cust_details_table.yview) 


        self.cust_details_table.heading("ref",text="refer no")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("mother",text="mother")
        self.cust_details_table.heading("gender",text="gender")
        self.cust_details_table.heading("post",text="post")
        self.cust_details_table.heading("mobile",text="mobile")
        self.cust_details_table.heading("email",text="email")
        self.cust_details_table.heading("nationality",text="nationality")
        self.cust_details_table.heading("idproof",text="ID proof")
        self.cust_details_table.heading("idnumber",text="ID number")
        self.cust_details_table.heading("address",text="Address")


        self.cust_details_table["show"]="headings"
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.fetch_data() 
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)


# insertinng data into database


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
                messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:
               
               conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into custo values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_ref.get(),
                                                                                self.var_cust_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_post.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_idproof.get(),
                                                                                self.var_idnumber.get(),
                                                                                self.var_address.get()



                                                                        )) 
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
                                                                               

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from custo")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:        
                self.cust_details_table.insert("",END,values=i)

            conn.commit()
            conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]


        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])                   

   #update button functionality



    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("error","please enter mobile number",parent=self.root)
        else:                
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update custo set name=%s,mother=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(
                                  
                                  
            
                                                                                                                                                                
                                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                                self.var_mother.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_post.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                self.var_idproof.get(),
                                                                                                                                                                self.var_idnumber.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_ref.get()        )) 
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","data updates succesfully")
            
        #except Exception as es:
         #       messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
                    




   #delete button functionality


    def mdelete(self):
        mdelete=messagebox.askyesno("HTM","do you want to delete this",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
            my_cursor=conn.cursor()
            query="delete from custo where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data
        conn.close()   






        #button reset functionality
                                                        
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
       # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
       # self.var_nationality.set(""),
       # self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_address.set("") 
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))  




        #search button functionality


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from custo where" +str(self.serch_var.get())+'"LIKE%"+str(self.txt_search.get())+"%"')
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()                                    


if __name__ == "__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()