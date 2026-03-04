N = int(input())

arr = list(map(int, input().split()))
arr.insert(0, 0)

dy = [1] * (N+1)

for i in range(2, N+1):
    for j in range(i-1, 0, -1):
        if arr[i] > arr[j]:
            dy[i] = max(dy[i], dy[j] + 1)

print(max(dy))