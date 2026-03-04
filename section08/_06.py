N = int(input())
arr = [[0, 0, 0]]
dy = [0]
# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2
# 밑면, 높이, 무게
#  0    1    2
for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x : x[0])

for i in range(N):
    dy.append(arr[i+1][1])

for i in range(2, N+1):
    for j in range(i-1, 0, -1):

        if arr[i][2] > arr[j][2]:
            dy[i] = max(dy[i], dy[j] + arr[i][1])

print(max(dy))