import sys

dy = [0, 0, -1]
dx = [-1, 1, 0]

graph = []
for i in range(10):
    graph.append(list(map(int, input().split())))

def dfs(y, x):
    for i in range(3):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy < 10 and 0 <= xx < 10 and graph[yy][xx] != 0:
            if yy == 0:
                print(xx)
                sys.exit()

            graph[yy][xx] = 0
            dfs(yy, xx)
            break

for i in range(10):
    if graph[9][i] == 2:
        dfs(9, i)