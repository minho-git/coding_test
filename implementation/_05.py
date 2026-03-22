N, M = map(int, input().split())

arr = [0] * (N+M+1)

for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i+j] += 1

answer = max(arr)

for index, value in enumerate(arr):
    if value == answer:
        print(index, end=" ")