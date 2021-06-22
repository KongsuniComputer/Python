import random

low = list()
mid = list()
high = list()


for i in range(0, 99):
    nansu = random.randint(1,100)

    if nansu < 40:
        low.append(nansu)
    elif 40 <= nansu < 70:
        mid.append(nansu)
    elif nansu >= 70:
        high.append(nansu)

low.sort()
mid.sort()
high.sort()

print("40미만의 값 : ", low)
print("40이상 70미만의 값 : ", mid)
print("70이상의 값 : ", high)
