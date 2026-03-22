N, M = map(int, input().split())
path = [0] * (M + 1)
res = 0

def dfs(level):
    global res

    if level == M+1:
        res += 1
        for j in range(1, M+1):
            print(path[j], end=" ")

        print()
        return

    for i in range(1, N+1):
        path[level] = i
        dfs(level+1)

dfs(1)
print(res)