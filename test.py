from struct import pack
from tkinter import *
from ttkbootstrap import *
from Estimation import est
from calcul import calcul
import os
os.system("cls")


def root():
 root = Toplevel(themename="yeti")
 def estimation():
     root.withdraw()
     est()
 def cal():
    root.config()

 root.title('BACalculator')

 root.geometry("720x404")
 root.maxsize(width = 720,height= 404)
 root.resizable(True,True)
 gif = PhotoImage(file=r"3.png")
 Label(root,image=gif).place(x=-2,y=-2)
 
 butti = Button(root,text=" Calculer la note du semestre",bootstyle="danger-solid",command=cal)
 butti1 = Button(root,text="Estimation de la note de BAC",bootstyle="danger-solid",command=estimation)
 
 butti.place(y=200,x=290)
 butti1.place(y=250,x=290)
 root.mainloop()
root()