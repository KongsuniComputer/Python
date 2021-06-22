#제작 : 20202068 이규하

import math

print("코로나 19로 인해 원격으로 미적분 수업을 하는 한 교실에서......\n\n")


print("선생님 : 오늘은 제 2 코사인 법칙에 대해 알아볼까요~~~~????\n")

answer1 = input("학생의 대답 : ")
i = 0
for i in range(0, 5):
    i = i + 1
    print(f'학생 {i} : ', answer1)

print("\n선생님 : 저번 시간에 배운 제 1 코사인 법칙에서 배웠던 식")
print("선생님 : a = ccosB+bcosC, b = ccosA+acosC, c = a cosB+bcosA 을 기억하죠?\n")

answer2 = input("학생의 대답 : ")
i = 0
for i in range(0, 5):
    i = i + 1
    print(f'학생 {i} : ', answer2)


print("\n선생님 : 오 좋아요! a=bcosC + ccosB, b = ccosA + acosC, c = acosB + bcosA 식의 양변에 각각 a, b, c를 곱해봐요")
print("선생님 : 그러면 a^2 = abcosC + accosB, b^2 = bccosA + abcosC, c^2 = bccosB + bccosA가 될거에요!\n")

print("선생님 : 이 세 식을 빼볼께요!")
print("선생님 : a^2−b^2−c2^2 = abcosC + accosB − bccosA − abcosC − accosB − bccosA = −2bccosA​ 이고")
print("선생님 : 정리해주면, a^2 = b^2 + c^2 − 2bccosA 가 되겠죠?\n")

answer3 = input("학생의 대답 : ")
i = 0
for i in range(0, 5):
    i = i + 1
    print(f'학생 {i} : ', answer3)


print("\n선생님 : 이게 바로 제 2 코사인 법칙 이에요!!!\n")
print("선생님 : 여러분들이 이해를 다 했으리라 믿고 선생님이 만든 프로그램을 하나 가져 왔어요!\n")

print("선생님 : 주어진 두변과 그 사이에 끼인 각으로 제 2 코사인 법칙을 이용해 문제를 해결하는 유용한 프로그램이죠!\n")

print("선생님 : 그럼 아래에 주어진 문제를 이 프로그램을 이용하여 해결해 볼까요??")
print("'문제는 (Question.png)를 참조하자'\n")

bc_length = float(input("변 BC 길이 입력 : "))
ac_length = float(input("변 AC 길이 입력 : "))
acb_degrees = int(input("각 ACB 크기 입력 : "))

acb_radians = math.radians(acb_degrees)

ab_length2 = float((bc_length ** 2 + ac_length ** 2) - (2 * bc_length * ac_length * math.cos(acb_radians)))

allanswer = round(ab_length2,2)

print("변 (AB)^2의 값은 :", allanswer ,"입니다!\n")

jinjjajinjja = str("진짜 " * 4)

print("\n\n선생님 : 우와~", jinjjajinjja,"잘했어요~~~\n")
print("선생님 : 오늘도 수고하셨습니다~~~ 다음시간에 뵈요~~!\n")

answer4 = input("학생의 대답 : ")
i = 0
for i in range(0, 5):
    i = i + 1
    print(f'학생 {i} : ', answer4)

print("\n\n\n - 수업 끝 -")

