from collections import deque

N = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

graph = []
_min = float("inf")
_max = float("-inf")


for i in range(N):
    tmp = list(map(int, input().split()))
    max_value = max(tmp)

    _max = max(_max, max_value)
    graph.append(tmp)

res = float("-inf")

# 높이 최소부터 최대까지
for i in range(_max+1):
    check = [[0] * N for _ in range(N)]
    q = deque()
    tmp = 0

    # 지도를 돌자.
    for y in range(N):
        for x in range(N):
            if check[y][x] == 0 and graph[y][x] > i:
                q.append((y, x))
                check[y][x] = 1
                tmp += 1

                # 영역을 돌자.
                while q:
                    now_y, new_x = q.popleft()

                    for k in range(4):
                        yy = now_y + dy[k]
                        xx = new_x + dx[k]

                        if 0 <= yy < N and 0 <= xx < N and graph[yy][xx] > i and check[yy][xx] == 0:
                            q.append((yy, xx))
                            check[yy][xx] = 1



    if res < tmp:
        res = tmp


print(res)

