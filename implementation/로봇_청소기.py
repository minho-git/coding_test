import sys

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []

dy = [-1, 0, 1, 0] # 북, 동, 남, 서
dx = [0, 1, 0, -1]

for i in range(N):
    graph.append(list(map(int, input().split())))

answer = 0

while True:

    if graph[r][c] == 0:
        graph[r][c] = -1
        answer += 1

    for i in range(4):
        rr = r + dy[(d+3-i) % 4]
        cc = c + dx[(d+3-i) % 4]

        if graph[rr][cc] == 0: # 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
            d = (d+3-i) % 4
            r = rr
            c = cc
            break

    else: # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        rr = r + dy[(d+2)%4]
        cc = c + dx[(d+2)%4]

        if graph[rr][cc] == 1:
            print(answer)
            sys.exit()
        else:
            r = rr
            c = cc
