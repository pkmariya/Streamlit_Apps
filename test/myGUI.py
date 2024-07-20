
from Tkinter import *
import tkMessageBox
import Tkinter
import calendar

top = Tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

C = Tkinter.Canvas(top, bg="palegreen", height=250, width=300)


coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="darkgreen")

C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, width = 20)

C2 = Checkbutton(top, text = "Value", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, width = 20)
C.pack()
C1.pack()
C2.pack()
top.mainloop()

