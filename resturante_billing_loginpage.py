from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import random
import datetime
from resturante_billing import Bill_App

win=Tk()
url = ImageTk.PhotoImage(Image.open("C:/Users/Admin/Pictures/download.jpg")) 
canvasl=Canvas(win,width=500,height=500)
canvasl.pack(fill="both",expand=True)
canvasl.create_image(0,0,image=url,anchor='nw')
win.title('Restaurant billing system')
win.geometry('2000x1000')
win.configure(bg='cyan')

class Myrest:
        
        def Mylogin(self):
                username=self.e1.get()
                password=self.e2.get()

                if username=="admin" and password=="admin":
                        messagebox.showinfo("","Login successfully")

                        root=Toplevel()
                        obj=Bill_App(root)
                        #self.root.geometry("1350x700+0+0")
                        root.mainloop()


                elif  username=="" and password=="":
                          messagebox.showinfo("","Need to enter anything")
                        
                else:
                        messagebox.showinfo("","Incorrect username and password")

        def __init__(self,win):

                self.lbl1=Label(win,text='username')
                self.lbl1.place(x=425, y=325)
                self.lbl2=Label(win,text='password')
                self.lbl2.place(x=425, y=375)
                  
                self.e1=Entry(bd=5)
                self.e2=Entry(bd=5,show='*')
                self.e1.place(x=525, y=325)
                self.e2.place(x=525, y=375)

                self.b1=Button(win, text='Submit', bg='blue',fg='white',command=self.Mylogin,bd=6).place(x=425, y=425)

mywin=Myrest(win)

