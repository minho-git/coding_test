import itertools
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))
M = int(input())
res = 0

for tmp in itertools.combinations(a, K):

    if sum(tmp) % M == 0:
        res += 1


print(res)




