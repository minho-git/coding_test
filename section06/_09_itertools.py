import sys
input = sys.stdin.readline

import itertools as it

N, F = map(int, input().split())
binary = [1] * N

for i in range(1, N):
    binary[i] = binary[i-1] * (N - i) // i

a = list(range(1,N+1))
for tmp in it.permutations(a):
    _sum = 0
    for index, value in enumerate(tmp):
        _sum += binary[index] * value

    if _sum == F:
        for x in tmp:
            print(x, end=" ")

        break

