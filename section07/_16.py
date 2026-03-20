import sys

dy = [0, 0, 1]
dx = [1, -1, 0]

graph = []
for i in range(10):
    graph.append(list(map(int, input().split())))

def dfs(y, x, start):

    for i in range(3):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy < 10 and 0 <= xx < 10 and graph[yy][xx] != 0:
            if graph[yy][xx] == 2:
                print(start)
                sys.exit()

            graph[yy][xx] = 0
            dfs(yy, xx, start)
            graph[yy][xx] = 1
            break

for i in range(10):
    if graph[0][i] == 1:
        graph[0][i] = 0 # 사전 핑퐁 차단!!
        dfs(0, i, i)