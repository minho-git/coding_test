import sys

input = sys.stdin.readline

N = int(input())
graph = [(0, 0)]
dp = [0] * (N+2)


for i in range(N):
    graph.append(tuple(map(int, input().split())))


for i in range(1, N+1):
    clear_day = i + graph[i][0]

    dp[i] = max(dp[i], dp[i-1])

    if clear_day <= N+1:
        dp[clear_day] = max(dp[clear_day], dp[i] + graph[i][1])

print(max(dp))