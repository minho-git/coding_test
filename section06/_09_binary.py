import sys

input = sys.stdin.readline

N, F = map(int, input().split())
graph = [0] * N
visited = [0] * (N+1)
binary = [1] * N

for i in range(1, N):
    binary[i] = (binary[i-1] * (N -i)) // i


def dfs(level, _sum):

    if level > N or _sum > F:
        return

    if level == N and _sum == F:
        for x in graph:
            print(x, end=" ")

        sys.exit()

    else:
        for j in range(1, N+1):
            if visited[j] == 0:
                visited[j] = 1
                graph[level] = j
                dfs(level+1, _sum + binary[level] * j)
                visited[j] = 0

dfs(0, 0)