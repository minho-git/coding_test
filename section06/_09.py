import sys

input = sys.stdin.readline

N, F = map(int, input().split())
graph = [0] * N
visited = [0] * (N+1)

def dfs(level):
    if level == N:
        copy_graph = graph[:]

        while len(copy_graph) > 1:
            next_graph = []
            for i in range(len(copy_graph)-1):
                next_graph.append(copy_graph[i] + copy_graph[i+1])

            copy_graph = next_graph

        if copy_graph[0] == F:
            for x in graph:
                print(x, end= " ")

            sys.exit()

    else:
        for i in range(1, N+1):
            if visited[i] == 0:
                visited[i] = 1
                graph[level] = i
                dfs(level+1)
                visited[i] = 0

dfs(0)