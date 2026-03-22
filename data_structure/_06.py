from collections import deque

# 5 2
# 60 50 70 80 90

N, M = map(int, input().split())
arr = list(map(int, input().split()))
que = deque()
count = 0

for i in range(N):
    que.append((i, arr[i]))

while True:
    _pop = que.popleft()

    if any(val > _pop[1] for pos, val in que):
        que.append(_pop)
    else:
        count += 1
        if _pop[0] == M:
            break

print(count)