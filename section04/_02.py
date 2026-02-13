# 0 ~ 최댓값
# 이분 분할 하면서 각 리스트 요소 나눠서 몫 더해서 N보다 크면 count랑 max 저장하기!!

K, N = map(int, input().split())
arr = []

for i in range(K):
    arr.append(int(input()))

s = 1 # 랜선 시작이 0일수는 없다. -> 1로 설정하기
e = max(arr)
res = 0

while s <= e:
    mid = (s + e) // 2
    tmp = 0
    for x in arr:
        tmp += x // mid

    if tmp >= N:
        res = mid
        s = mid + 1
    elif tmp < N:
        e = mid - 1

print(res)

