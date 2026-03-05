N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(tuple(map(int,input().split())))

dy = [0] * (M+1)

for i in range(len(arr)):
    for j in range(M, arr[i][1] - 1, -1):
        dy[j] = max(dy[j], dy[j-arr[i][1]] + arr[i][0])


print(max(dy))


