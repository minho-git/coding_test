import sys

input = sys.stdin.readline

N = int(input()) # 개수
coins = list(map(int, input().split()))
M = int(input()) # 금액
res = float("inf")

coins.sort(reverse=True) # coin이 오름차순으로 주어진다는 말은 없다.

def dfs(count, total):
    global res

    if count > res or total > M:
        return

    if total == M:
        if count < res:
            res = count

        return

    for coin in coins:
        dfs(count + 1, total + coin)

dfs(0, 0)

print(res)

