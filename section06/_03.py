N = int(input())
check = [0] * (N + 1)

def dfs(v):

    if v > N:
        if sum(check) > 0:
            for i in range(1, N + 1):
                if check[i] == 1:
                    print(i, end=" ")

            print()
        return

    check[v] = 1
    dfs(v+1)
    check[v] = 0
    dfs(v+1)

dfs(1)
