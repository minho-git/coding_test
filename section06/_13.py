import sys; input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
res = 0
for i in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1

def dfs(node):
    global res

    if node == N:
        res += 1
        for x in path:
            print(x, end=" ")
        print()

    else:
        for x in range(1, N+1):
            if graph[node][x] == 1 and visited[x] == 0:
                visited[x] = 1
                path.append(x)
                dfs(x)
                path.pop()
                visited[x] = 0

visited[1] = 1
path = [1]
dfs(1)
print(res)