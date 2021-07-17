from tkinter import* 

from tkinter import ttk

from PIL import Image,ImageTk  

from tkinter import messagebox

from hotel import hotelmanagementsystem



class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1530x800+0+0")

        img1=Image.open(r"H:\WhatsApp\login4.jpg")
        img1=img1.resize((1530,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_bg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbl_bg.place(x=0,y=0,width=1530,height=800)


#label frame login frame

        labelframeleft=LabelFrame(self.root,bd=2,bg="black",relief=RIDGE ,padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=610,y=170,width=340,height=450) 
        

        #root.attributes('-alpha',0.5)
        
          


#logo

        img2=Image.open(r"H:\WhatsApp\login.png")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl_logo=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbl_logo.place(x=730,y=175,width=100,height=100)


        get_str=Label(labelframeleft,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)


#label


        username=lbl=Label(labelframeleft,text="UserName",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=65,y=155)



        self.txtuser=ttk.Entry(labelframeleft,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)




#password 

        password=lbl=Label(labelframeleft,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=65,y=225)



        self.txtpass=ttk.Entry(labelframeleft,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=260,width=270)



        #icon image



        img3=Image.open(r"H:\WhatsApp\username.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)



        lbl_logo1=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lbl_logo1.place(x=650,y=332,width=25,height=25)
      
      
      
      
        img4=Image.open(r"H:\WhatsApp\pass.png")
        img4=img4.resize((25,25),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbl_logo3=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        lbl_logo3.place(x=650,y=402,width=25,height=25)



# login button


        loginbtn=Button(labelframeleft,text="LOGIN",command=self.login,font=("times new roman",15,"bold"),bd=5,relief=RIDGE,fg="black",bg="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

#register button


        regbtn=Button(labelframeleft,text="NEW USER REGISTER",command=self.register,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black")
        regbtn.place(x=25,y=350,width=160)

    
        


                         

#for got password

        passbtn=Button(labelframeleft,text="Forgot-Password",command=self.register,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black")
        passbtn.place(x=25,y=370,width=160)



    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields are required")
                
        elif self.txtuser.get()=="diwesh" or self.txtpass.get()=="rai":
           # messagebox.showinfo("succesfull","welcome")
            #self.new_window=Toplevel(self.root)
            self.app=hotelmanagementsystem(self.root)
            messagebox.showinfo("succesfull","welcome")
       # else:
        #    open_main=messagebox.askyesno("YesNo","Access only admin")        
         #   if open_main>0:
          #      self.new_window=Toplevel(self.root)
           #     self.app=hotelmanagementsystem(self.root)
            #else:
             #   if not open_main:
              #      return

                                 


                    
    def register(self):
        messagebox.showerror("error","error 404 ")                        


                        


 



if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()