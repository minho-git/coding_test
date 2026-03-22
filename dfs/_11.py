N, K = map(int, input().split()) # 총 갯수, 뽑는 갯수
res = 0
arr = list(map(int, input().split()))
M = int(input()) # 배수

def dfs(level, start, _sum):
    global res

    if level == K:
        if _sum % M == 0:
            res += 1

    else:
        for i in range(start, N):
            dfs(level+1, i+1, _sum + arr[i])


dfs(0, 0, 0)
print(res)

# 10번 11번 다시 풀어보기!
