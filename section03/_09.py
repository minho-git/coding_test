N = int(input())

arr = [[0] * (N+2) for _ in range(N+2)]
res = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


for i in range(1, N+1):
    arr[i][1:N+1] = list(map(int,input().split()))

for i in range(1, N+1):
    for j in range(1, N+1):
        if all(arr[i][j] > arr[i+dy[k]][j+dx[k]] for k in range(4)): # all 방식도 있다. 여러번 봐서 눈에 익히기!
            res += 1

print(res)

# all이라는 함수와 방향 배열 기억하기

