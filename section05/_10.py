import heapq

h = []

while True:
    num = int(input())

    if num == -1:
        break
    elif num == 0:
        if len(h) == 0:
            print(-1)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, num)


