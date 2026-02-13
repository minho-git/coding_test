N, M = map(int, input().split())
arr = list(map(int, input().split()))

tot = arr[0]
count = 0

lt = 0
rt = 1

while True:
    if tot < M:
        if rt < N:
            tot += arr[rt]
            rt += 1
        else:
            break
    elif tot == M:
        count += 1
        tot -= arr[lt]
        lt += 1
    else:
        tot -= arr[lt]
        lt += 1

print(count)

# M = 3
#
#   lt
# 1  2  1  3  1  1  1  2
#       rt
#
# sum은 lt ~ rt -1 까지 합
# sum = 3
# count = 1

# if sum > M 보다 크면 lt 빼고 줄이기
# if sum == M 이면 count += 1 하고 lt 빼고 줄이기
# if sum < M  이면 rt 늘리기

# 만약에