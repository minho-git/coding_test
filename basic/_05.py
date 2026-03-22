# 1. 1부터 N 까지 홀수 출력하기
N = int(input())
# for i in range(1, N+1):
#     if i % 2 == 1:
#         print(i)

# 2. 1부터 N 까지 합 출력하기
# total = 0
# for i in range(1, N+1):
#     total += i
#
# print(total)

# 3. N 의 약수 출력하기
for i in range(1, N+1):
    if N % i == 0:
        print(i, end=" ")