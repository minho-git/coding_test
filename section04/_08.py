N, M = map(int, input().split())
res = 0

arr = list(map(int, input().split()))
arr.sort()

while len(arr) > 1:
    tmp = arr[0] + arr[-1]
    if tmp <= M:
        arr.pop(0)

    arr.pop(-1)
    res += 1

if len(arr) == 1:
    res += 1

print(res)
