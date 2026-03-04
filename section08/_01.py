# F(n) = F(n-1) + F(n-2)

# 5m -> 3 + 5 = 8개
# 4m -> 5개
# 3m -> 3개
# 2m -> 2개
# 1m -> 1개

N = int(input())

arr = [0] * (N+1)
arr[1] = 1
arr[2] = 2

for i in range(3, N+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[N])