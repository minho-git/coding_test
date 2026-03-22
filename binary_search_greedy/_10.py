# 입력
# 8
# 5 3 4 0 2 1 1 0
# 결과
# 4 8 6 2 5 1 3 7


# 뒤에서 부터 시작해서 res에 추가해보자.
# 8
# 8 7
# 8 6 7
# 8 6 5 7
# 4 8 6 5 7
# 4 8 6 5 3 7
# 4 8 6 2 5 3 7
# 4 8 6 2 5 1 3 7

# 오케이 그냥 앞에 갯수만 세서 넣자!!!

N = int(input())
arr = list(map(int, input().split()))
res = []

for i in range(N, 0, -1):
    res.insert(arr[i-1], i)

for x in res:
    print(x, end=" ")