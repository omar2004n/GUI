from this import d
from tkinter import *
import os,time,sys
from attr import s
from ttkbootstrap import *
from entries import result

def resource_path(relative_path):

    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def PC():

 root = Toplevel("yeti")
 backg = resource_path("calc.png")
 gif = PhotoImage(file=backg)
 Label(root,image=gif).place(x=-2,y=-2)
 z = 306
 mat1 = Entry(root,bootstyle="secondary")
 mat2 = Entry(root,bootstyle="secondary")
 mat3 = Entry(root,bootstyle="secondary")

 pc1 = Entry(root,bootstyle="secondary")
 pc2 = Entry(root,bootstyle="secondary")
 pc3 = Entry(root,bootstyle="secondary")
 pc4 = Entry(root,bootstyle="secondary")

 svt1 = Entry(root,bootstyle="secondary")
 svt2 = Entry(root,bootstyle="secondary")
 svt3 = Entry(root,bootstyle="secondary")

 ar1 = Entry(root,bootstyle="secondary")
 ar2 = Entry(root,bootstyle="secondary")
 ar3 = Entry(root,bootstyle="secondary")

 fr1 = Entry(root,bootstyle="secondary")
 fr2 = Entry(root,bootstyle="secondary")
 fr3 = Entry(root,bootstyle="secondary")
 fr4 = Entry(root,bootstyle="secondary")
 fr5 = Entry(root,bootstyle="secondary")



 ph1 = Entry(root,bootstyle="secondary")
 ph2 = Entry(root,bootstyle="secondary")
 ph3 = Entry(root,bootstyle="secondary")

 sp1 = Entry(root,bootstyle="secondary")
 sp2 = Entry(root,bootstyle="secondary")
 sp3 = Entry(root,bootstyle="secondary")

 eng1 = Entry(root,bootstyle="secondary")
 eng2 = Entry(root,bootstyle="secondary")
 eng3 = Entry(root,bootstyle="secondary")

 ei1 = Entry(root,bootstyle="secondary")
 ei2 = Entry(root,bootstyle="secondary")
 ei3 = Entry(root,bootstyle="secondary")

 mat1.place(x= z, y=147-15 ,width=50)
 mat2.place(x= z+100, y= 147-15,width=50)
 mat3.place(x= z+200, y=147-15,width=50)

 pc1.place(x= z, y= 191-15,width=50)
 pc2.place(x= z+100, y= 191-15,width=50)
 pc3.place(x= z+200, y= 191-15,width=50)
 pc4.place(x= z+300, y= 191-15,width=50)

 svt1.place(x=z , y= 237-15,width=50)
 svt2.place(x=z+100 , y= 237-15,width=50)
 svt3.place(x= z+200, y= 237-15,width=50)

 ar1.place(x=z , y= 270-15,width=50)
 ar2.place(x=z+100 , y= 270-15,width=50)
 ar3.place(x=z+200 , y= 270-15,width=50)

 fr1.place(x=z , y= 310-15,width=50)
 fr2.place(x=z+100 , y= 310-15,width=50)
 fr3.place(x=z+200 , y= 310-15,width=50)
 fr4.place(x=z+300 , y= 310-15,width=50)
 fr5.place(x=z+400 , y= 310-15,width=50)

 

 ph1.place(x=z , y= 350-15,width=50)
 ph2.place(x=z+100 , y= 350-15,width=50)
 ph3.place(x=z+200 , y= 350-15,width=50)

 sp1.place(x=z , y= 386-15,width=50)
 sp2.place(x=z+100 , y= 386-15,width=50)
 sp3.place(x=z+200 , y= 386-15,width=50)

 eng1.place(x=z , y= 426-15,width=50)
 eng2.place(x= z+100, y= 426-15,width=50)
 eng3.place(x=z+200 , y= 426-15,width=50)

 ei1.place(x=z , y= 464-15,width=50)
 ei2.place(x=z+100 , y= 464-15,width=50)
 ei3.place(x= z+200, y= 464-15,width=50)
 

 
 mat1,mat2,mat3, pc1,pc2,pc3,pc4, svt1,svt2,svt3, ar1,ar2,ar3, fr1,fr2,fr3,fr4, ph1,ph2,ph3,sp1,sp2,sp3,eng1,eng2,eng3,ei1,ei2,ei3
 mathent = [mat1,mat2,mat3]
 pcent  =[ pc1,pc2,pc3,pc4]
 svtent = [svt1,svt2,svt3]
 arent = [ ar1,ar2,ar3]
 frent = [ fr1,fr2,fr3,fr4,fr5]
 phent = [ ph1,ph2,ph3]
 spent = [sp1,sp2,sp3]
 engent = [eng1,eng2,eng3]
 eient = [ei1,ei2,ei3]
 subjects = [mathent,svtent,arent,phent,spent,engent,eient,pcent,frent]
 coefficient = [7,5,2,2,4,2,2,7,4]
 def next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"
 def prev_widget(event):
        event.widget.tk_focusPrev().focus()
        return "break"
 def sumy():
   global matsu,pcsu,svtsu,phsu,arsu,engsu,frsu,eisu,spsu
   matsu = float(mat1.get())+float(mat2.get())+float(mat3.get())
   matx = matsu/3
   pcsu = float(pc1.get())+float(pc2.get())+float(pc3.get())+float(pc4.get())
   pcx =pcsu/4
   svtsu = float(svt1.get())+float(svt2.get())+float(svt3.get())
   svtx = svtsu/3
   phsu = float(ph1.get())+float(ph2.get())+float(ph3.get())
   phx = phsu/3
   arsu = float(ar1.get())+float(ar2.get())+float(ar3.get())
   arx = arsu/3
   engsu = float(eng1.get())+float(eng2.get())+float(eng3.get())
   engx = engsu/3
   frsu = float(fr1.get())+float(fr2.get())+float(fr3.get())+float(fr4.get())+float(fr5.get())
   frx = frsu/5
   eisu = float(ei1.get())+float(ei2.get())+float(ei3.get())
   eix = eisu/3
   spsu = float(sp1.get())+float(sp2.get())+float(sp3.get())
   spx = spsu/3

   matsu = matx*7
   pcsu =pcx*7
   svtsu = svtx*5
   phsu = phx*7
   arsu = arx*2
   engsu = engx*2
   frsu = frx*4
   eisu = eix*2
   spsu = spx*4
   s = matsu+pcsu+svtsu+phsu+arsu+engsu+frsu+eisu+spsu
   s = s/40
   
   result(s,matx,pcx,svtx,phx,arx,engx,frx,eix,spx)


 
 button = Button(root,text="Submit",bootstyle="secondary-solid",command=sumy)
 button.place(y=500,x=403)
 root.title("BACalculator")
 root.resizable(False,False)
 mat1.bind("<Right>",next_widget)
 mat2.bind("<Right>",next_widget)
 mat3.bind("<Right>",next_widget)
 pc1.bind("<Right>",next_widget)
 pc2.bind("<Right>",next_widget)
 pc3.bind("<Right>",next_widget)
 pc4.bind("<Right>",next_widget)

 svt1.bind("<Right>",next_widget)
 svt2.bind("<Right>",next_widget)
 svt3.bind("<Right>",next_widget)

 ar1.bind("<Right>",next_widget)
 ar2.bind("<Right>",next_widget)
 ar3.bind("<Right>",next_widget)
 fr1.bind("<Right>",next_widget)
 fr2.bind("<Right>",next_widget)
 fr3.bind("<Right>",next_widget)
 fr4.bind("<Right>",next_widget)
 fr5.bind("<Right>",next_widget)



 ph1.bind("<Right>",next_widget)
 ph2.bind("<Right>",next_widget)
 ph3.bind("<Right>",next_widget)

 sp1.bind("<Right>",next_widget)
 sp2.bind("<Right>",next_widget)
 sp3.bind("<Right>",next_widget)

 eng1.bind("<Right>",next_widget)
 eng2.bind("<Right>",next_widget)
 eng3.bind("<Right>",next_widget)

 ei1.bind("<Right>",next_widget)
 ei2.bind("<Right>",next_widget)
 ei3.bind("<Right>",next_widget)
 mat1.bind("<Left>",prev_widget)
 mat2.bind("<Left>",prev_widget)
 mat3.bind("<Left>",prev_widget)
 pc1.bind("<Left>",prev_widget)
 pc2.bind("<Left>",prev_widget)
 pc3.bind("<Left>",prev_widget)
 pc4.bind("<Left>",prev_widget)

 svt1.bind("<Left>",prev_widget)
 svt2.bind("<Left>",prev_widget)
 svt3.bind("<Left>",prev_widget)

 ar1.bind("<Left>",prev_widget)
 ar2.bind("<Left>",prev_widget)
 ar3.bind("<Left>",prev_widget)
 fr1.bind("<Left>",prev_widget)
 fr2.bind("<Left>",prev_widget)
 fr3.bind("<Left>",prev_widget)
 fr4.bind("<Left>",prev_widget)
 fr5.bind("<Left>",prev_widget)


 ph1.bind("<Left>",prev_widget)
 ph2.bind("<Left>",prev_widget)
 ph3.bind("<Left>",prev_widget)

 sp1.bind("<Left>",prev_widget)
 sp2.bind("<Left>",prev_widget)
 sp3.bind("<Left>",prev_widget)

 eng1.bind("<Left>",prev_widget)
 eng2.bind("<Left>",prev_widget)
 eng3.bind("<Left>",prev_widget)

 ei1.bind("<Left>",prev_widget)
 ei2.bind("<Left>",prev_widget)
 ei3.bind("<Left>",prev_widget)
 button.bind("<Left>",prev_widget)
 button.bind("<Right>",next_widget)


 root.geometry("950x548")


 root.mainloop()
##########################################################################################################
############################################################################################################
#############################################################################################################
def SVT():

 root = Toplevel("yeti")
 backg = resource_path("calc.png")
 gif = PhotoImage(file=backg)
 Label(root,image=gif).place(x=-2,y=-2)
 z = 306
 mat1 = Entry(root,bootstyle="secondary")
 mat2 = Entry(root,bootstyle="secondary")
 mat3 = Entry(root,bootstyle="secondary")

 pc1 = Entry(root,bootstyle="secondary")
 pc2 = Entry(root,bootstyle="secondary")
 pc3 = Entry(root,bootstyle="secondary")
 

 svt1 = Entry(root,bootstyle="secondary")
 svt2 = Entry(root,bootstyle="secondary")
 svt3 = Entry(root,bootstyle="secondary")
 svt4 = Entry(root,bootstyle="secondary")

 ar1 = Entry(root,bootstyle="secondary")
 ar2 = Entry(root,bootstyle="secondary")
 ar3 = Entry(root,bootstyle="secondary")

 fr1 = Entry(root,bootstyle="secondary")
 fr2 = Entry(root,bootstyle="secondary")
 fr3 = Entry(root,bootstyle="secondary")
 fr4 = Entry(root,bootstyle="secondary")
 fr5 = Entry(root,bootstyle="secondary")


 ph1 = Entry(root,bootstyle="secondary")
 ph2 = Entry(root,bootstyle="secondary")
 ph3 = Entry(root,bootstyle="secondary")

 sp1 = Entry(root,bootstyle="secondary")
 sp2 = Entry(root,bootstyle="secondary")
 sp3 = Entry(root,bootstyle="secondary")

 eng1 = Entry(root,bootstyle="secondary")
 eng2 = Entry(root,bootstyle="secondary")
 eng3 = Entry(root,bootstyle="secondary")

 ei1 = Entry(root,bootstyle="secondary")
 ei2 = Entry(root,bootstyle="secondary")
 ei3 = Entry(root,bootstyle="secondary")

 mat1.place(x= z, y=147-15 ,width=50)
 mat2.place(x= z+100, y= 147-15,width=50)
 mat3.place(x= z+200, y=147-15,width=50)

 pc1.place(x= z, y= 191-15,width=50)
 pc2.place(x= z+100, y= 191-15,width=50)
 pc3.place(x= z+200, y= 191-15,width=50)
 svt4.place(x= z+300, y= 237-15,width=50)

 svt1.place(x=z , y= 237-15,width=50)
 svt2.place(x=z+100 , y= 237-15,width=50)
 svt3.place(x= z+200, y= 237-15,width=50)

 ar1.place(x=z , y= 270-15,width=50)
 ar2.place(x=z+100 , y= 270-15,width=50)
 ar3.place(x=z+200 , y= 270-15,width=50)

 fr1.place(x=z , y= 310-15,width=50)
 fr2.place(x=z+100 , y= 310-15,width=50)
 fr3.place(x=z+200 , y= 310-15,width=50)
 fr4.place(x=z+300 , y= 310-15,width=50)
 fr5.place(x=z+400 , y= 310-15,width=50)

 

 ph1.place(x=z , y= 350-15,width=50)
 ph2.place(x=z+100 , y= 350-15,width=50)
 ph3.place(x=z+200 , y= 350-15,width=50)

 sp1.place(x=z , y= 386-15,width=50)
 sp2.place(x=z+100 , y= 386-15,width=50)
 sp3.place(x=z+200 , y= 386-15,width=50)

 eng1.place(x=z , y= 426-15,width=50)
 eng2.place(x= z+100, y= 426-15,width=50)
 eng3.place(x=z+200 , y= 426-15,width=50)

 ei1.place(x=z , y= 464-15,width=50)
 ei2.place(x=z+100 , y= 464-15,width=50)
 ei3.place(x= z+200, y= 464-15,width=50)
 

 
 mat1,mat2,mat3, pc1,pc2,pc3,svt4, svt1,svt2,svt3, ar1,ar2,ar3, fr1,fr2,fr3,fr4, ph1,ph2,ph3,sp1,sp2,sp3,eng1,eng2,eng3,ei1,ei2,ei3
 mathent = [mat1,mat2,mat3,]
 pcent  =[ pc1,pc2,pc3,]
 svtent = [svt1,svt2,svt3,svt4]
 arent = [ ar1,ar2,ar3]
 frent = [ fr1,fr2,fr3,fr4,fr5]
 phent = [ ph1,ph2,ph3]
 spent = [sp1,sp2,sp3]
 engent = [eng1,eng2,eng3]
 eient = [ei1,ei2,ei3]
 subjects = [mathent,svtent,arent,phent,spent,engent,eient,pcent,frent]
 coefficient = [7,5,2,2,4,2,2,7,4]
 def next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"
 def prev_widget(event):
        event.widget.tk_focusPrev().focus()
        return "break"
 def sumy():
   global matsu,pcsu,svtsu,phsu,arsu,engsu,frsu,eisu,spsu
   matsu = float(mat1.get())+float(mat2.get())+float(mat3.get())
   matx = matsu/3
   pcsu = float(pc1.get())+float(pc2.get())+float(pc3.get())
   pcx =pcsu/3
   svtsu = float(svt1.get())+float(svt2.get())+float(svt3.get())+float(svt4.get())
   svtx = svtsu/4
   phsu = float(ph1.get())+float(ph2.get())+float(ph3.get())
   phx = phsu/3
   arsu = float(ar1.get())+float(ar2.get())+float(ar3.get())
   arx = arsu/3
   engsu = float(eng1.get())+float(eng2.get())+float(eng3.get())
   engx = engsu/3
   frsu = float(fr1.get())+float(fr2.get())+float(fr3.get())+float(fr4.get())+float(fr5.get())
   frx = frsu/5
   eisu = float(ei1.get())+float(ei2.get())+float(ei3.get())
   eix = eisu/3
   spsu = float(sp1.get())+float(sp2.get())+float(sp3.get())
   spx = spsu/3

   matsu = matx*7
   pcsu =pcx*5
   svtsu = svtx*7
   phsu = phx*7
   arsu = arx*2
   engsu = engx*2
   frsu = frx*4
   eisu = eix*2
   spsu = spx*4
   s = matsu+pcsu+svtsu+phsu+arsu+engsu+frsu+eisu+spsu
   s = s/40
   
   result(s,matx,pcx,svtx,phx,arx,engx,frx,eix,spx)


 
 button = Button(root,text="Submit",bootstyle="secondary-solid",command=sumy)
 button.place(y=500,x=403)
 root.title("BACalculator")
 root.resizable(False,False)
 mat1.bind("<Right>",next_widget)
 mat2.bind("<Right>",next_widget)
 mat3.bind("<Right>",next_widget)
 pc1.bind("<Right>",next_widget)
 pc2.bind("<Right>",next_widget)
 pc3.bind("<Right>",next_widget)
 svt4.bind("<Right>",next_widget)

 svt1.bind("<Right>",next_widget)
 svt2.bind("<Right>",next_widget)
 svt3.bind("<Right>",next_widget)

 ar1.bind("<Right>",next_widget)
 ar2.bind("<Right>",next_widget)
 ar3.bind("<Right>",next_widget)

 fr1.bind("<Right>",next_widget)
 fr2.bind("<Right>",next_widget)
 fr3.bind("<Right>",next_widget)
 fr4.bind("<Right>",next_widget)
 fr5.bind("<Right>",next_widget)



 ph1.bind("<Right>",next_widget)
 ph2.bind("<Right>",next_widget)
 ph3.bind("<Right>",next_widget)

 sp1.bind("<Right>",next_widget)
 sp2.bind("<Right>",next_widget)
 sp3.bind("<Right>",next_widget)

 eng1.bind("<Right>",next_widget)
 eng2.bind("<Right>",next_widget)
 eng3.bind("<Right>",next_widget)

 ei1.bind("<Right>",next_widget)
 ei2.bind("<Right>",next_widget)
 ei3.bind("<Right>",next_widget)
 mat1.bind("<Left>",prev_widget)
 mat2.bind("<Left>",prev_widget)
 mat3.bind("<Left>",prev_widget)
 pc1.bind("<Left>",prev_widget)
 pc2.bind("<Left>",prev_widget)
 pc3.bind("<Left>",prev_widget)
 svt4.bind("<Left>",prev_widget)

 svt1.bind("<Left>",prev_widget)
 svt2.bind("<Left>",prev_widget)
 svt3.bind("<Left>",prev_widget)

 ar1.bind("<Left>",prev_widget)
 ar2.bind("<Left>",prev_widget)
 ar3.bind("<Left>",prev_widget)

 fr1.bind("<Left>",prev_widget)
 fr2.bind("<Left>",prev_widget)
 fr3.bind("<Left>",prev_widget)
 fr4.bind("<Left>",prev_widget)
 fr5.bind("<Left>",prev_widget)

 ph1.bind("<Left>",prev_widget)
 ph2.bind("<Left>",prev_widget)
 ph3.bind("<Left>",prev_widget)

 sp1.bind("<Left>",prev_widget)
 sp2.bind("<Left>",prev_widget)
 sp3.bind("<Left>",prev_widget)

 eng1.bind("<Left>",prev_widget)
 eng2.bind("<Left>",prev_widget)
 eng3.bind("<Left>",prev_widget)

 ei1.bind("<Left>",prev_widget)
 ei2.bind("<Left>",prev_widget)
 ei3.bind("<Left>",prev_widget)
 button.bind("<Left>",prev_widget)
 button.bind("<Right>",next_widget)

 
 root.geometry("950x548")


 root.mainloop()