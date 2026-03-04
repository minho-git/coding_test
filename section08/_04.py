N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dy = [1] * (N+1)

for i in range(2, N+1):
    for j in range(1, i):
        if arr[i] > arr[j]:
            dy[i] = max(dy[i], dy[j] + 1)


# 나(arr[i])보다 작은 애들 중에서 제일 잘나가는 애(max(dy[j])) 뒤에 줄 서면 나도 덩달아 길어진다!
print(max(dy))

