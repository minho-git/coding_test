import sys; input = sys.stdin.readline
from collections import deque

S, E = map(int, input().split())

# 직선의 좌표 점은 1부터 10,000
check = [0] * 10001 # 이게 문제!! 이동하면서 공간을 넘을 수 있다.
q = deque()
arr = [1, -1, 5]
q.append((S, 0))
check[S] = 1

while True:
    pos, level = q.popleft()

    if pos == E:
        print(level)
        break
    else:
        for x in arr:
            next_pos = pos + x
            if 1 <= next_pos <= 10000 and check[next_pos] == 0: # 순서 다시 생각하자!!
                q.append((next_pos, level+1))
                check[next_pos] = 1