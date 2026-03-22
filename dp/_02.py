N = int(input())
arr = [0] * (N+1)
arr[1] = 1
arr[2] = 2

def dfs(v):
    if arr[v] != 0:
        return arr[v]

    arr[v] = dfs(v-1) + dfs(v-2)
    return arr[v]

print(dfs(N))