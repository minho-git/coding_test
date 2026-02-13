arr = [list(map(int, input().split())) for _ in range(7)]
res = 0

for i in range(7):
    for j in range(3):
        tmp = arr[i][j:j+5]
        if tmp == tmp[::-1]:
            res += 1

        for k in range(2):
            if arr[j+k][i] != arr[j+4-k][i]:
                break
        else:
            res += 1


print(res)