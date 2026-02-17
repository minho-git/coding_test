N, M = map(int, input().split())
arr = list(map(int, input().split()))

def check(capacity):
    count = 1
    sum_val = 0
    for x in arr:

        if sum_val + x > capacity:
            count += 1
            sum_val = x
        else:
            sum_val += x

    return count

s = max(arr)
e = sum(arr)
res = 0

while s <= e:
    mid = (s + e) // 2
    cnt = check(mid)

    if cnt <= M: # 17이 되면 23도 된다!!!
        res = mid
        e = mid - 1
    else:
        s = mid + 1

print(res)