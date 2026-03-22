# 함수 만들기

# 여러 값을 반환하면 튜플로 반환
def add(a, b):
    c = a + b
    d = a - b
    return c, d


# print(add(3, 2))

# 소수만 출력
a = [12, 13, 7, 9, 19, 1, 3]

def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**(1/2)) + 1))


for num in a:
    if is_prime(num):
        print(num, end=" ")






