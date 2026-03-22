N = int(input())
arr = map(int, input().split())
_max = float("-inf")
answer = 0

def digit_sum(x: int) -> int:
    # _sum = 0
    #
    # while x != 0:
    #     _sum += x % 10
    #     x //= 10
    # return _sum

    return sum(map(int, str(x)))

for i in arr:
    tmp = digit_sum(i)
    if tmp > _max:
        _max = tmp
        answer = i

print(answer)
