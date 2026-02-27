import sys; input = sys.stdin.readline
from collections import deque

N = int(input())
graph = []
visited = [[0] * N for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    graph.append(list(map(int, input().split())))

q = deque()
q.append((N//2, N//2, 0))
visited[N//2][N//2] = 1
res = graph[N//2][N//2]

while q:
    y, x, level = q.popleft()

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if  level < N//2 and visited[new_y][new_x] == 0:
            q.append((new_y, new_x, level + 1))
            res += graph[new_y][new_x]
            visited[new_y][new_x] = 1

print(res)