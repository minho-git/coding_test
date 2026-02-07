def reverse(x):
    # tmp = str(x)
    # tmp = tmp[::-1]
    # return int(tmp)
    x = int(x)
    res = 0
    while x > 0:
        tmp = x % 10
        res = res * 10 + tmp
        x //= 10

    return res



def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(x**(1/2) + 1)):
        if x % i == 0:
            return False
    else:
        return True


N = int(input())
arr = list(map(int,input().split()))

for num in arr:
    reversed_num = reverse(num)
    if is_prime(reversed_num):
        print(reversed_num, end=" ")
