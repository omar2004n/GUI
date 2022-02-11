from tkinter import *
from ttkbootstrap import *

def result(resultat,matx,pcx,svtx,phx,arx,engx,frx,eix,spx):
    result = Toplevel("superhero")
    result.geometry("300x650")
    matz = Label(result,text="Math : "+str(round(matx,2)),foreground="black",font=("designero",20),justify=LEFT)
    pcz = Label(result,text="Physique Chimie : "+str(round(pcx,2)),foreground="black",font=("designero",20),justify=LEFT)
    svtz = Label(result,text="SVT : "+str(round(svtx,2)),foreground="black",font=("designero",20))
    phz = Label(result,text="Philosophie : "+str(round(phx,2)),foreground="black",font=("designero",20))
    arz = Label(result,text="Arabe : "+str(round(arx,2)),foreground="black",font=("designero",20))
    engz = Label(result,text="English : "+str(round(engx,2)),foreground="black",font=("designero",20))
    frz = Label(result,text="Francais : "+str(round(frx,2)),foreground="black",font=("designero",20))
    eiz = Label(result,text="E.Islamic : "+str(round(eix,2)),foreground="black",font=("designero",20))
    spz = Label(result,text="Sport : "+str(round(spx,2)),foreground="black",font=("designero",20))
    res = Label(result,text="Bilan : "+str(round(resultat,2)),foreground="red",font=("designero",20))

    matz.pack(side=TOP)
    pcz.pack(side=TOP)
    svtz.pack(side=TOP)
    phz.pack(side=TOP) 
    arz.pack(side=TOP)
    engz.pack(side=TOP)
    frz.pack(side=TOP)
    eiz.pack(side=TOP)
    spz.pack(side=TOP)
    res.pack(side=TOP,ipady=10)

    result.mainloop()
