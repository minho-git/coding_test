graph = [[1] * 9 for _ in range(9)]
res = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(1, 8):
    graph[i][1:8] = list(map(int, input().split()))

# 출발 시작점 체크하는거 까먹지 말기
graph[1][1] = 1

def dfs(y, x):
    global res

    if y == 7 and x == 7:
        res += 1

    else:
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]

            if graph[new_y][new_x] == 0:
                graph[new_y][new_x] = 1
                dfs(new_y, new_x)
                graph[new_y][new_x] = 0

dfs(1, 1)
print(res)

