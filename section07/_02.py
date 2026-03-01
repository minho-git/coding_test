import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = []
res = 0
for i in range(N):
    arr.append(list(map(int, input().split())))

def dfs(day, salary):
    global res

    if day == N:
        if res < salary:
            res = salary

    else:
        dfs(day + 1, salary)

        # 돌다리도 두드리고 건너기!! 저지르고 보면 안돼요.
        if day + arr[day][0] <= N:
            dfs(day + arr[day][0], salary + arr[day][1])

dfs(0,0)
print(res)