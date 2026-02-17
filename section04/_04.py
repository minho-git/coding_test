N, C = map(int, input().split())
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()

def check(capacity):
    _cnt = 1
    std = arr[0]

    for j in range(1, N):
        if arr[j] - std >= capacity: # 크거나 같아야 말을 놓을 수 있다.
            _cnt += 1
            std = arr[j]

    return _cnt


s = 1
e = arr[-1] - arr[0] # arr[-1] -> 마지막 값
res = 1

while s <= e:
    mid = (s + e) // 2

    cnt = check(mid)

    if cnt >= C:
        res = mid
        s = mid + 1
    else:
        e = mid - 1

print(res)