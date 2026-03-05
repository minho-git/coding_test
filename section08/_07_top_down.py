import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = []
check = [[0] * N for _ in range(N)]

for i in range(N):
    graph.append(list(map(int,input().split())))

def dfs(y, x):
    if check[y][x] != 0:
        return check[y][x]

    if y == 0 and x == 0:
        return graph[0][0]
    elif y == 0:
        check[y][x] = dfs(0, x-1) + graph[y][x]
    elif x == 0:
        check[y][x] = dfs(y-1, 0) + graph[y][x]
    else:
        check[y][x] = min(dfs(y-1, x), dfs(y, x-1)) + graph[y][x]

    return check[y][x]

print(dfs(N-1, N-1))
