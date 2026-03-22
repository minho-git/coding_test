graph = []
_min = float("inf")
_max = float("-inf")
start = tuple()
end = tuple()
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
res = 0


N = int(input())

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if _min > graph[i][j]:
            _min = graph[i][j]
            start = (i, j)

        if _max < graph[i][j]:
            _max = graph[i][j]
            end = (i, j)

def dfs(y, x):
    global res

    if y == end[0] and x == end[1]:
        res += 1

    else:
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if 0 <= yy < N and 0 <= xx < N and graph[yy][xx] > graph[y][x]:
                dfs(yy, xx)


dfs(start[0], start[1])
print(res)
