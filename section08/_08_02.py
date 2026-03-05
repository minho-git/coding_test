N, M = map(int, input().split())
arr = []
dy = [0] * (M+1)

for i in range(N):
    arr.append(tuple(map(int,input().split())))

# for i in range(M, 0, -1):
#     for j in range(len(arr)):
#
#         tmp = i - arr[j][0]
#         if tmp >= 0:
#             dy[tmp] = max(dy[tmp], dy[i] + arr[j][1])

for i in range(M):
    for j in range(len(arr)):

        tmp = i + arr[j][0]
        if tmp <= M:
            dy[tmp] = max(dy[tmp], dy[i] + arr[j][1])

print(max(dy))

