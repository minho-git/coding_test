# 리스트와 내장함수(1)
import random

# b = list()
# print(b)

a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0])

b = list(range(1, 11))
# print(b)

c = a + b
# print(c)

# print(a)
a.append(6)
# print(a)

a.insert(3, 7) # 3번 index에 7이 들어가는 것.
# print(a)

a.pop()
# print(a)

a.pop(3) #pop 하고 싶은 index 지정 가능.
# print(a)

# 리스트에서 특정 값을 지울 수 있다.
a.remove(4) # 값 4를 제거.
# print(a)

# print(a.index(5))

a = list(range(1, 11))
# print(a)
# print(sum(a)) # a라는 리스트의 모든 원소를 더해준다.
# print(max(a)) # a라는 리스트의 최댓값을 반환한다.
# print(min(a)) # a라는 리스트의 최솟값을 반환한다.
# print(min(7, 5))
# max나 min은 인자 값들 중에 최솟값을 반환한다.

# 리스트를 섞어보자.
random.shuffle(a)
print(a)
a.sort() # 오름차순
print(a)
a.sort(reverse=True) # 내림차순
print(a)
a.clear()
print(a)