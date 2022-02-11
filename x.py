from struct import pack
from tkinter import *
from ttkbootstrap import *
from Estimation import est
from result import branche
import os
import sys
os.system("cls")


def root():
 def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
 root = Window(themename="yeti")
 def estimation():
     root.withdraw()
     est()
 def cal():
     root.withdraw()
     branche()

 root.title('BACalculator')

 root.geometry("720x404")
 root.maxsize(width = 720,height= 404)
 root.resizable(True,True)
 backg = resource_path("manic.png")
 gif = PhotoImage(file=backg)
 Label(root,image=gif).place(x=-2,y=-2)
 
 butti = Button(root,text=" Calculer la note du semestre",bootstyle="danger-solid",command=cal)
 butti1 = Button(root,text="Estimation de la note de BAC",bootstyle="danger-solid",command=estimation)
 
 butti.place(y=200,x=290)
 butti1.place(y=250,x=290)
 root.mainloop()
root()