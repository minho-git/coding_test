N, M = map(int, input().split())
visited = [0] * (N + 1)
graph = [0] * (N + 1)
res = 0

def dfs(level):
    global res

    if level == M+1:
        res += 1

        for j in range(1, M+1):
            print(graph[j], end=" ")

        print()
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            graph[level] = i
            dfs(level+1)
            visited[i] = 0

dfs(1)
print(res)