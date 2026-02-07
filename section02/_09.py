# 풀이 1번
#
# N = int(input())
# answer = 0
#
# for i in range(N):
#     arr = [0] * 7
#     nums = list(map(int, input().split()))
#
#     for num in nums:
#         arr[num] += 1
#
#     max_count = max(arr)
#     price = 0
#
#     if max_count == 3:
#         for j in range(1, 7):
#             if arr[j] == 3:
#                 price = 10000 + (j * 1000)
#     elif max_count == 2:
#         for j in range(1, 7):
#             if arr[j] == 2:
#                 price = 1000 + (j * 100)
#     elif max_count == 1:
#         max_num = 0
#         for j in range(1, 7):
#             if arr[j] == 1:
#                 if max_num > j:
#                     max_num = j
#
#             price = j * 100
#
#     if price > answer:
#         answer = price
#
#
# print(answer)



# 풀이 2번
#
# N = int(input())
# answer = 0
#
# for i in range(N):
#     nums = list(map(int, input().split()))
#     arr = [[i, 0] for i in range(0, 7)]
#     price = 0
#
#     for num in nums:
#         if arr[num][1] == 0:
#             arr[num] = [num, 1]
#         else:
#             arr[num][1] += 1
#
#     arr.sort(key=lambda x : (x[1], x[0]), reverse=True)
#
#     if arr[0][1] == 3:
#         price = 10000 + (arr[0][0] * 1000)
#     elif arr[0][1] == 2:
#         price = 1000 + (arr[0][0] * 100)
#     else:
#         price = arr[0][0] * 100
#
#     if price > answer:
#         answer = price
#
# print(answer)


# 풀이 3번
N = int(input())
answer = 0
for i in range(N):

    arr = list(map(int, input().split()))
    price = 0

    arr.sort()
    if arr[0] == arr[2]: # 같은 주사위 3개
        price = 10000 + (arr[0] * 1000)

    elif arr[0] != arr[1] and arr[1] != arr[2]: # 같은 주사위 X
        price = arr[2] * 100

    else: # 같은 주사위 2개
        price = 1000 + (arr[1] * 100)

    if answer < price:
        answer = price

print(answer)