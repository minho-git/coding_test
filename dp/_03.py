N = int(input())
check = [0] * (N+1)

def dfs(v):
    if check[v] != 0:
        return check[v]

    if v <= 2:
        return v

    check[v] = dfs(v-1) + dfs(v-2)
    return check[v]


print(dfs(N))