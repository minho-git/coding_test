N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = N - 1

arr.sort()

while s <= e:
    mid = (s + e) // 2

    if arr[mid] == M:
        print(mid+1)
        break
    elif arr[mid] > M:
        e = mid - 1
    else:
        s = mid + 1

