from tkinter import *
import os,sys
from tkinter import font
from ttkbootstrap import *



def est():
 def resource_path(relative_path):

    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
 root = Toplevel()
 root.title("BACalculator")
 root.resizable(False,False)
 root.geometry("950x548")
 backg = resource_path("est.png")
 gif = PhotoImage(file=backg)
 Label(root,image=gif).place(x=-2,y=-2)
 root.config(background='#c3c9c5',)
 ent1 = Entry(root,font="normal",exportselection=True,bootstyle="dark")
 ent2 = Entry(root,font="normal",exportselection=True,bootstyle="dark")
 ent3 = Entry(root,font="normal",exportselection=True,bootstyle="dark")
 def next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"
 def prev_widget(event):
        event.widget.tk_focusPrev().focus()
        return "break"
 def got():
    T = float(ent3.get())
    reg = float(ent2.get())
    con = float(ent1.get())
    R = reg*0.25
    C = con*0.25
    natx = T-R-C
    nat = natx/0.5
    res = Label(root
    ,text=str(round(nat,2))+"   ",font=("tahoma"))
    z = True

    if T>20 or reg>20 or con>20 :
       
       z= False
    if z :
     res.place(x=470,y=420)

 submit = Button(root,text="Submit",bootstyle="secondary-outline",command=got)
 ent1.bind("<Right>",next_widget)
 ent1.bind("<Left>",prev_widget)
 ent2.bind("<Right>",next_widget)
 ent2.bind("<Left>",prev_widget)
 ent3.bind("<Right>",next_widget)
 ent3.bind("<Left>",prev_widget)
 submit.bind("<Right>",next_widget)
 submit.bind("<Left>",prev_widget)

 ent1.bind("<Down>",next_widget)
 ent1.bind("<Up>",prev_widget)
 ent2.bind("<Down>",next_widget)
 ent2.bind("<Up>",prev_widget)
 ent3.bind("<Down>",next_widget)
 ent3.bind("<Up>",prev_widget)
 submit.bind("<Down>",next_widget)
 submit.bind("<Up>",prev_widget)
 



 ent1.place(x=450,y=195)
 ent2.place(x=450,y=260)
 ent3.place(x=450,y=320)
 submit.place(x=520,y=360)

 #bexit.place(x=660,y=330)
 root.mainloop()
