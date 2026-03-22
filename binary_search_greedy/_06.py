N = int(input())
arr = []
count = 0

for i in range(N):
    height, weight = map(int, input().split())
    arr.append((height, weight))

arr.sort(key=lambda x : x[0], reverse=True)
_max = 0


for x, y in arr:
    if y > _max:
        _max = y
        count += 1


print(count)