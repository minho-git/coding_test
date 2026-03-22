import sys; input = sys.stdin.readline
from collections import deque

graph = [[1] * 9 for _ in range(9)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for i in range(1, 8):
    graph[i][1:8] = list(map(int, input().split()))

q = deque()
q.append((1, 1, 0))
graph[1][1] = 1

while q:
    y, x, level = q.popleft()

    if y == 7 and x == 7:
        print(level)
        sys.exit()

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if graph[new_y][new_x] == 0:
            q.append((new_y, new_x, level+1))
            graph[new_y][new_x] = 1

print(-1)