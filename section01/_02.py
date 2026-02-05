# # 변수 입력(키보드로 입력)
# a = input("숫자를 입력하세요: ")
# print(a)

# a, b = input("숫자를 입력하세요 : ").split()
# print(type(a))
# print(a + b) # a, b는 string -> 연결됨.

# 숫자로 더할려면 어떻게 해야할까?
# a, b = input("숫자를 입력하세요 : ").split()
# a = int(a)
# b = int(b)
# print(type(a))
# print(a + b)

# 위에가 불편하다. -> map 내장함수 사용
# int도 내장함수
# a, b = map(int, input("숫자를 입력하세요 : ").split())
# print(a + b)
# print(a**b) # 거듭제곱

# a = 4.3 # 실수
# b = 3 # 정수
# c = a + b # 더 큰 범위로 변환됨.
# print(c)
# print(type(c))