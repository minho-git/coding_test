import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())
K = int(input())

arr = []
res = 0
total = 0
for i in range(K):
    arr.append(list(map(int, input().split())))
    total += arr[i][1] * arr[i][0]

def dfs(level, price, remain_amount):
    global res

    if price + remain_amount < T:
        return

    if level == K:
        if price == T:
            res += 1
    else:
        for c in range(arr[level][1] + 1):
            tmp = price + arr[level][0] * c
            if tmp <= T:
                dfs(level + 1, tmp, remain_amount - arr[level][0] * arr[level][1])

dfs(0, 0, total)
print(res)