import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = []
res = float("inf")

for i in range(N):
    arr.append(int(input()))

def dfs(level, a, b, c):
    global res

    if level == N:
        tmp = set()
        tmp.add(a)
        tmp.add(b)
        tmp.add(c)

        # 3개 같은지 확인 방법 -> set 활용하기
        if len(tmp) == 3:
            max_a = max(a, b, c)
            max_b = min(a, b, c)

            res = min(max_a - max_b, res)

    else:
        dfs(level+1, a + arr[level], b, c)
        dfs(level+1, a, b + arr[level], c)
        dfs(level+1, a, b, c + arr[level])

dfs(0,0, 0 ,0)
print(res)