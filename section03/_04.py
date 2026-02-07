N = int(input())
arr1 = list(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))

# 풀이 1
# 이미 정렬되어있다는 걸 신경 안쓰고 정렬한 방식
# 시간복잡도: O(n+m) * log(n+m)
# result = arr1 + arr2
# result.sort()
#
# print(result)

# 풀이 2
# 이미 정렬되어있다는 걸 활용해보자.
# 투포인터 방식 사용
# 시간복잡도: O(n+m)

result = []
p1 = 0
p2 = 0

while p1 < N and p2 < M:

    if arr1[p1] < arr2[p2]:
        result.append(arr1[p1])
        p1 += 1
    else:
        result.append(arr2[p2])
        p2 += 1

# while p1 < N:
#     result.append(arr1[p1])
#     p1 += 1

# while p2 < M:
#     result.append(arr2[p2])
#     p2 += 1

if p1 < N:
    result += arr1[p1:]

if p2 < N:
    result += arr2[p2:]

for x in result:
    print(x, end=" ")
