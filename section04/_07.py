N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()

for i in range(M):
    arr[0] += 1
    arr[-1] -= 1
    arr.sort()

print(arr[-1] - arr[0])

