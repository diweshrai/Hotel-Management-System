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



class RoomDetails:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")


        lbl_title=Label(self.root,text="ROOM DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

#label frame roomdetails

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add " ,padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=540,height=350)    



#logo

        img2=Image.open(r"H:\WhatsApp\2.png")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=100,height=50)

#labels and entry




        self.var_floor=StringVar()
        self.var_roomNo=StringVar()
        self.var_RoomType=StringVar()



#romm details 


#floor

        lbl_floor=Label(labelframeleft,text="floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20 ,font=("times new roman",13,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)



#room no
        
        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=20 ,font=("times new roman",13,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)

#room type

        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        combo_Roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_RoomType,font=("arial",12,"bold"),width=18,state="readonly")
        combo_Roomtype["value"]=("Single","Double","luxury")
        combo_Roomtype.grid(row=2,column=1)
        combo_Roomtype.current(0)

        #enty_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20 ,font=("times new roman",13,"bold"))
        #enty_RoomType.grid(row=2,column=1,sticky=W)


# BUTTONS


        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=440,height=40)


        #add button
        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btnadd.grid(row=0,column=0)



        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btnupdate.grid(row=0,column=1)

        

        btndelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btndelete.grid(row=0,column=2)


        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",13,"bold"),width=10,bg="black",fg="gold")
        btnreset.grid(row=0,column=3)


#label frame show roomdetails

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details " ,padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=600,y=55,width=650,height=350)    


        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
       
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
       
        scroll_y.config(command=self.room_table.yview) 

  
        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")
        
        

        self.room_table["show"]="headings"


        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)    
        self.room_table.column("roomType",width=100)


        self.room_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)



        # insertinng data into database


    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
                messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:
               
               conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into details values (%s,%s,%s)",(
                                                                           self.var_floor.get(),
                                                                           self.var_roomNo.get(),
                                                                           self.var_RoomType.get()
                                                                           
                                                                            






                                                                        )) 
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("success","New Room Added Succesfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)




      #fetch data                                                                          

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:        
                self.room_table.insert("",END,values=i)

            conn.commit()
            conn.close()

#get data 



    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]


        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])
       

 

 #update button functionality



    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("error","please enter contact number",parent=self.root)
        else:                
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                  
                                  
            
                                                                                                                                                                
                                                                                                                                                                 
                                                                           self.var_floor.get(),
                                                                           self.var_RoomType.get(),
                                                                           self.var_roomNo.get()
                                                                                   )) 
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
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data
        conn.close()   




         #button reset functionality
                                                        
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")
        


if __name__ == "__main__":
    root=Tk()
    obj=RoomDetails(root)
    root.mainloop()