# 람다 함수 (익명 함수, 람다 표현식)

# def plus_one(x: int) -> int:
#     return x+1
#
# plus_two = lambda x : x + 2
#
#
# print(plus_one(4))
# print(plus_two(4))

# 여기까지는 사용 방법
# 주로 내장 함수의 인자로 많이 사용됨
a = [1, 2, 3]
print(list(map(lambda x : x+1, a)))
#               함수명          이터레이터

b = [(3, 1), (2, 4), (5, 2)]
b.sort(key=lambda x : x[0])
print(b)