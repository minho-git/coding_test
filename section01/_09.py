# 리스트와 내장함수(2)

a = [23, 12, 36, 53, 19]
# print(a[:3])
# print(a[1:4])
# print(len(a))
#
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
#
# for x in a:
#     print(x, end=" ")
# print()

# 처음봅니다.
# for x in enumerate(a): #(0, 23) index와 value에 동시에 접근 가능. 튜플형태로 x로 넘겨줌.
#     print(x)

# 튜플
b = (1, 2, 3, 4, 5)
# print(b)
# print(b[0])

# 리스트와 다른 점은 요소 변경 불가.
# b[0]= 7

# for x in enumerate(a):
#     print(x[0], ":", x[1])

# 보통 이렇게 많이 사용
# for index, value in enumerate(a):
#     print(index, value)

if all(50>x for x in a):
    print(True)
else:
    print(False)

if any(15>x for x in a):
    print(True)
else:
    print(False)
