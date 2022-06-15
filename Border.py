from cProfile import label
from tkinter import *
from time import monotonic
import sys

window = Tk()
window.title("")
Time = monotonic()  
if monotonic() - Time < 3: 
 lbl = Label(window, text="Выполнено", font=("Arial Bold", 50), bg="black", fg="red")
 lbl.grid(column=0, row=0)  
 if monotonic() - Time >= 3: 
  lbl.destroy()
 
window.mainloop()