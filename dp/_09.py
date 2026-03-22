N = int(input())
arr = list(map(int, input().split()))
v = int(input())

# dp에서는 초기화가 진짜 중요하다.
dy = [float("inf")] * (v+1)
dy[0] = 0

for i in range(N):
    for j in range(arr[i], v+1):
        dy[j] = min(dy[j], dy[j-arr[i]] + 1)

print(dy[v])
