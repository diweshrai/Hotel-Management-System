from tkinter import ttk

from tkinter import* 

from PIL import Image,ImageTk  

from tkinter import messagebox


class report:
    def __init__(self,root):
        self.root=root
        self.root.title("report")
        self.root.geometry("1295x550+230+220")



        
        img1=Image.open(r"H:\WhatsApp\login2.jpg")
        img1=img1.resize((1295,700),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbling=Label(self.root,image=self.photoimg1,bd=10,relief=RIDGE)
        lbling.place(x=0,y=0,width=1295,height=550)


        self.var_name=StringVar()
        self.var_phone=StringVar()
        self.var_problem=StringVar()

#label frame report

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Report Your Problem" ,padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=400,y=100,width=455,height=210) 



#your name

        lbl_cust_ref=Label(labelframeleft,text="Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_name,width=29 ,font=("times new roman",13,"bold"))
        enty_ref.grid(row=0,column=1)

#phone number

        lbl_cust_ref=Label(labelframeleft,text="Phone Number",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_phone,width=29 ,font=("times new roman",13,"bold"))
        enty_ref.grid(row=1,column=1)


#problem
        lbl_cust_ref=Label(labelframeleft,text="Report Your Problem",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=2,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_problem,width=29 ,font=("times new roman",13,"bold"))
        enty_ref.grid(row=2,column=1)
  

 #submit and reset button
        btnsubmit=Button(labelframeleft,text="Reset",font=("arial",13,"bold"),width=10,bg="black",fg="gold",command=self.reset)
        btnsubmit.grid(row=4,column=0)


        btnreset=Button(labelframeleft,text="Submit",font=("arial",13,"bold"),width=10,bg="black",fg="gold",command=self.submit)
        btnreset.grid(row=4,column=1)


#reset button functionality


    def submit(self):
        if self.var_name.get()=="":
            messagebox.showerror("error","please enter your name",parent=self.root)

        elif self.var_problem.get()=="":
            messagebox.showerror("error","please enter the problem",parent=self.root)    


        elif self.var_phone.get()=="":
            messagebox.showerror("error","please enter Phone number",parent=self.root)
       
        else:
            messagebox.showinfo("Submit","Data Submited successfully")


    def reset(self):
      
        self.var_name.set("") 
        self.var_phone.set("")
        self.var_problem.set("")










if __name__ == "__main__":
    root=Tk()
    obj=report(root)
    root.mainloop()