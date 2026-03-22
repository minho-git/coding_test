# 먼저 회전을 시키자. 그리고 모래시계에 얼만큼 있는지 찾자!!

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
M = int(input())
res = 0

# 회전
for i in range(M):
    a, b, c = map(int,input().split())
    tmp = list(arr[a-1])

    if b == 0:
        # for j in range(N):
        #     # arr[a - 1][j] = tmp[(j + N - c) % 5]
        #     arr[a-1][(j - c) % N] = tmp[j]
        for _ in range(c):
            arr[a-1].append(arr[a-1].pop(0))
    else:
        # for j in range(N):
        #     # arr[a - 1][j] = tmp[(j + c) % N]
        #     arr[a-1][(j + c) % N] = tmp[j]
        for _ in range(c):
            arr[a - 1].insert(0, arr[a - 1].pop())

 # 갯수 세기
s = 0
e = N - 1

for y in range(N):
    res += sum(arr[y][s:e+1])

    if y < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1


print(res)

