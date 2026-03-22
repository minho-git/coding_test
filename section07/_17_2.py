N, M = map(int, input().split())
graph = []
res = float("inf")

for i in range(N):
    graph.append(list(map(int, input().split())))

pizza = []
house = []
cb = [0] * M

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            pizza.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))

def get_distance():
    global res

    distance = [float("inf")] * len(house)
    for i in range(len(house)):
        y, x = house[i]

        for j in cb:
            tmp = abs(y - pizza[j][0]) + abs(x - pizza[j][1])
            distance[i] = min(distance[i], tmp)

    res = min(res, sum(distance))

def dfs(start, level):
    if level == M:
        get_distance()
    else:
        for i in range(start, len(pizza)):
            cb[level] = i
            dfs(i+1, level+1)


dfs(0, 0)
print(res)















