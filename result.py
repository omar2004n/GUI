from struct import pack
from tkinter import *
from ttkbootstrap import *
from Estimation import est
import os,sys
from calcul import PC,SVT

def branche():
 br = Toplevel("yeti")
 def pc():
     br.withdraw()
     PC()
 def svt():
     br.withdraw()
     SVT()
 br.title('BACalculator')
 def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
 br.geometry("720x404")
 br.maxsize(width = 720,height= 404)
 br.resizable(True,True)
 backg = resource_path("manic.png")
 gif = PhotoImage(file=backg)
 Label(br,image=gif).place(x=-2,y=-2)
 
 butti = Button(br,text="2 Bac   Sc.Physique",bootstyle="danger-solid",command=pc)
 butti1= Button(br,text="2 Bac   Sc.Vie Terre",bootstyle="danger-solid",command=svt)
 
 butti.place(y=200,x=290)
 butti1.place(y=250,x=290)
 br.mainloop()

