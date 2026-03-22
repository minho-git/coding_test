import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = []
res = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

def dfs(level, score, _time):
    global res

    if _time > M:
        return

    if level == N:
        if score > res:
            res = score
    else:
        dfs(level + 1, score + arr[level][0], _time + arr[level][1])
        dfs(level + 1, score, _time)

dfs(0, 0, 0)

print(res)

