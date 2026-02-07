N = int(input())

arr = list(map(int, input().split()))

# 풀이1: 배열 수정
# answer = arr[0]
#
# for i in range(1, N):
#     if arr[i] != 0:
#         arr[i] = arr[i-1] + 1
#         answer += arr[i]
#
# print(answer)

# 풀이2: 가중치를 따로 빼기
answer = 0
cnt = 0

for i in range(N):
    if arr[i] == 1:
        cnt += 1
        answer += cnt

    else:
        cnt = 0

print(answer)