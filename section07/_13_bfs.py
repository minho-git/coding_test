from collections import deque

N = int(input())
graph = []
res = 0

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = 0
            q = deque()
            q.append((i, j))
            res += 1

            while q:
                y, x = q.popleft()

                for k in range(8):
                    yy = y + dy[k]
                    xx = x + dx[k]

                    if 0 <= yy < N and 0 <= xx < N and graph[yy][xx] == 1:
                        q.append((yy, xx))
                        graph[yy][xx] = 0

print(res)