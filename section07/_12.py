import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())

graph = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
arr = []

for i in range(N):
    graph.append(list(map(int, input().rstrip())))

def dfs(y, x):
    count = 1

    for k in range(4):
        yy = y +dy[k]
        xx = x +dx[k]

        if 0 <= yy < N and 0 <= xx < N and graph[yy][xx] == 1:
            graph[yy][xx] = 0
            count += dfs(yy, xx)

    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = 0
            arr.append(dfs(i, j))

arr.sort()
print(len(arr))

for num in arr:
    print(num)

