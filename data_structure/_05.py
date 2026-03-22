from collections import deque

N, K = map(int, input().split())
que = deque()
count = 0

for i in range(1, N+1):
    que.append(i)


while len(que) != 1:
    _pop = que.popleft()
    count += 1

    if count % K != 0:
        que.append(_pop)

print(que.popleft())




