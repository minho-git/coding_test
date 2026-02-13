N = int(input())
arr = [[0] * (N+1) for i in range(N + 1)]
_max = 0

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    arr[i][1:] = tmp

for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        tmp += arr[j][i]

    _max = max(_max, tmp)

    tmp = 0
    for j in range(1, N + 1):
        tmp += arr[i][j]

    _max = max(_max, tmp)

tmp = 0
for j in range(1, N + 1):
    tmp += arr[j][j]

_max = max(_max, tmp)

tmp = 0
for j in range(1, N + 1):
    tmp += arr[N - j + 1][j]

_max = max(_max, tmp)

print(_max)
