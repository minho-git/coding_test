# 259 5
# 81
# 58
# 42
# 33
# 61

C, N = map(int, input().split())
arr = []
res = 0

for i in range(N):
    arr.append(int(input()))

total = sum(arr)

def dfs(level, _sum, before):
    global res, total

    # 이 가지치기로만은 부족하다.
    # 더 강한 가지치기를 생각해보자.
    # 현재 값에서 남은 거 다 더해도 max보다 작으면 굳이 들어갈 필요가 없다.
    # 남은 것들 합을 어떻게 구할까?
    # 매개변수로 하나 만들자. 지금까지 나왔던 것들의 합을 넘기는 것이다.

    if _sum > C or res > total - before + _sum:
        return

    if level == N:
        if res < _sum:
            res = _sum

        return

    dfs(level + 1, _sum + arr[level], before + arr[level])
    dfs(level + 1, _sum, before + arr[level])



dfs(0, 0, 0)

print(res)