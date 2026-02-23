import sys; input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    s, e, v = map(int, input().split())

    graph[s][e] = v

for i in range(1,N+1):
    for j in range(1, N+1):
        print(graph[i][j], end=" ")
    print()