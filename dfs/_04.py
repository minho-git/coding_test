N = int(input())
arr = list(map(int, input().split()))
flag = False
total = sum(arr)

def dfs(v, _sum):
    global flag

    if flag or _sum > total // 2:
        return

    if v == N:
        if _sum == total // 2:
            flag = True

        return

    dfs(v+1, _sum + arr[v])
    dfs(v+1, _sum)



dfs(0, 0)

if flag:
    print("YES")
else:
    print("NO")
