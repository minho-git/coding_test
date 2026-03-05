N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

dy = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):

        if i == 0 and j == 0:
            dy[i][j] = graph[i][j]
        elif i == 0:
            dy[i][j] = dy[i][j-1] + graph[i][j]
        elif j == 0:
            dy[i][j] = dy[i-1][j] + graph[i][j]
        else:
            dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + graph[i][j]


print(dy[N-1][N-1])