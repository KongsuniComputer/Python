#HELLO 여러분 모두 반갑습니다!

import turtle 
t = turtle.Turtle() 
  
t.width(3) 
t.speed(5) 
  

# 문자 H 
t.left(90) 
t.forward(70) 
t.penup() 
t.goto(0, 35) 
t.pendown() 
t.right(90) 
t.forward(30) 
t.penup() 
t.goto(30, 70) 
t.pendown() 
t.right(90) 
t.forward(70) 
  
# 문자 E 
t.penup() 
t.goto(40, 0) 
t.pendown() 
t.right(180) 
t.forward(70) 
t.right(90) 
t.forward(35) 
t.penup() 
t.goto(40, 35) 
t.pendown() 
t.forward(35) 
t.penup() 
t.goto(40, 0) 
t.pendown() 
t.forward(35) 
  
# 문자 L 
t.penup() 
t.goto(90, 70) 
t.pendown() 
t.right(90) 
t.forward(70) 
t.left(90) 
t.forward(35) 
  
# 문자 L 
t.penup() 
t.goto(135, 70) 
t.pendown() 
t.right(90) 
t.forward(70) 
t.left(90) 
t.forward(35) 
  
# 문자 O 
t.penup() 
t.goto(210, 70) 
t.pendown() 
for i in range(25): 
    t.right(15) 
    t.forward(10) 
