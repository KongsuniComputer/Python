import turtle as t
import random

def race() :
    t1.pendown() 
    t2.pendown() 
    t1.speed(1)
    t2.speed(1)
    for i in range(100):
        d1 = random.randint(1, 12) 
        t1.forward(d1) 
        d2 = random.randint(1, 12) 
        t2.fd(d2)
        
s = t.Screen()
image1 = "car1.gif"
image2 = "car2.gif"
s.addshape(image1)
s.addshape(image2)
t.onkeypress(race, "space")         

t1 = t.Turtle()       # 첫 번째 거북이
t1.hideturtle()
t1.shape(image1)
t1.pencolor('black')
t1.pensize(10)      
t1.penup()
t1.goto(-300, 0)
t1.showturtle()

t2 = t.Turtle()      # 두 번째 거북이
t2.hideturtle()
t2.shape(image2)
t2.pencolor('red')
t2.pensize(10) 
t2.penup()
t2.goto(-300, -200)
t2.showturtle()

t.listen()                     # 사용자가 키를 입력하기를 기다리도록 함.
t.mainloop()


 

