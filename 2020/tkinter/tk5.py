from tkinter import *

window=Tk()
window.geometry("+800+400")

sum=0
price = {'사   과':500, '우   유':1000, '소고기':5000}

def process1():
  global value1
  selection = lbox1.curselection()
  value1 = price[ lbox1.get(selection[0])]
  
 
 
def process2():
  global sum
  selection = lbox2.curselection()
  value2 = lbox2.get(selection[0])[0]
  sum = sum + value1 * int(value2)
  l2['text'] = sum
 

l0 = Label(window, text="구입할 품목과 수량을 선택하세요", height=2)
l0.grid(row=0, column=0, columnspan=4)

lbox1 = Listbox(window, selectmode="browse", width=0, height=0)
lbox1.insert(0, "사   과")
lbox1.insert(1, "우   유")
lbox1.insert(2, "소고기")
lbox1.grid(row=1, column=0)

lbox2 = Listbox(window, selectmode="browse", width=0, height=0)
lbox2.insert(0, "1개")
lbox2.insert(1, "2개")
lbox2.insert(2, "3개")
lbox2.insert(3, "4개")
lbox2.grid(row=1, column=2)

 
b1 = Button(window, text="수량", command=process1)
b2 = Button(window, text="추가", command=process2)
b1.grid(row=1, column=1)
b2.grid(row=1, column=3)

l1 = Label(window, text="결재액 :", height=2)
l2 = Label(window, text=sum, height=2)
l1.grid(row=2, column=0)
l2.grid(row=2, column=1)

window.mainloop()


