import random

n1 = random.randint(0,100)
n2 = random.randint(0,100)
n3 = random.randint(0,100)
n4 = random.randint(0,100)


a = list()
b = list()


if n1 >= 50:
 a.append(n1)  
else:
 b.append(n1)  

if n2 >= 50:
 a.append(n2)  
else:
 b.append(n2)  

if n3 >= 50:
 a.append(n3)  
else:
 b.append(n3)  

if n4 >= 50:
 a.append(n4)  
else:
 b.append(n4)
 

print("50 이상 : ", a)
print("50 미만 : ", b)
