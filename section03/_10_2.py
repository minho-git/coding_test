arr = [list(map(int, input().split())) for _ in range(9)]
arr.insert(0, [0] * 10)
for i in range(1, 10):
    arr[i].insert(0, 0)

for i in range(1, 10):
    row = [0] * 10
    col = [0] * 10

    for j in range(1, 10):
        row[arr[i][j]] = 1
        col[arr[j][i]] = 1

    if sum(row) != 9 or sum(col) != 9:
        print("NO")
        exit()

for i in range(1, 4):
    for j in range(1, 4):
        rect = [0] * 10
        for k in range(1, 4):
            for q in range(1, 4):
                rect[arr[(i-1)*3 + k][(j-1)*3 + q]] = 1

        if sum(rect) != 9:
            print("NO")
            exit()