N, M = map(int, input().split())
arr = []
dy = [0] * (M+1)

for i in range(N):
    arr.append(tuple(map(int,input().split())))

for i in range(len(arr)):
    for j in range(arr[i][0], M+1):
        dy[j] = max(dy[j], dy[j-arr[i][0]] + arr[i][1])

print(max(dy))

