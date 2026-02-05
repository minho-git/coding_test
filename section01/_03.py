# 조건문 if(분기, 중첩)

# x = 7
# if x == 7:
#     print("lucky")
#     print("ㅋㅋㅋㅋ")


# x = 5
# if x != 7:
#     print("lucky")
#     print("ㅋㅋㅋㅋㅋ")

# x = 2
# if x >= 10:
#     if x % 2 == 1:
#         print("x는 10 이상의 홀수")
#     else:
#         print("x는 10 이상의 짝수")
# else:
#     print("x는 10 미만")

# x = 7
# if 0 < x < 10: # x > 0 and x < 10 이랑 같다. 파이썬은 축약 가능!!!
#     print("x는 10 미만의 자연수")


x = 78
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")