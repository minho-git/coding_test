from collections import deque

arr = list(input())
N = int(input())

for i in range(N):
    order = deque(arr)
    plan = input()

    for subject in plan:
        if subject in order and subject != order.popleft():
            print(f"#{i+1} NO")
            break
    else:
        # 필수과목 들었는지 꼭 확인해야 한다.
        if order:
            print(f"#{i + 1} NO")
        else:
            print(f"#{i + 1} YES")





