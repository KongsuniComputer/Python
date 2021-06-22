from tkinter import *

window=Tk()
window.geometry("+800+400")

sum=0
 
def process1():
  global sum
  selection = lbox.curselection()
  value = lbox.get(selection[0])
  sum= sum + int(value)
  l2['text'] = sum
 
 
def process2():
  global sum
  selection = lbox.curselection()
  value = lbox.get(selection[0])
  sum = sum - int(value)
  l2['text'] = sum
 
def process3():
  global sum
  sum = 0
  l2['text'] = sum
 
l1 = Label(window, text="잔고 :", height=2)
l2 = Label(window, text=sum, height=2)
l1.grid(row=0, column=0)
l2.grid(row=0, column=1)
 
lbox = Listbox(window, width=10, height=0, selectmode="browse")
lbox.insert(0, "  10000")
lbox.insert(1, "  20000")
lbox.insert(2, "  30000")
lbox.grid(row=1, column=0, rowspan=3)

 
b1 = Button(window, text="입   금", command=process1)
b2 = Button(window, text="출   금", command=process2)
b3 = Button(window, text="초기화", command=process3)
 
b1.grid(row=1, column=1)
b2.grid(row=2, column=1)
b3.grid(row=3, column=1)
 
window.mainloop()


