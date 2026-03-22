# 행, 열, 네모 리스트를 각각 만들자.
row = [[0] * 10 for _ in range(10)]
col = [[0] * 10 for _ in range(10)]
rect = [[0] * 10 for _ in range(10)]

# 입력받자.
arr = [list(map(int, input().split())) for _ in range(9)]
arr.insert(0, [0] * 10)
for i in range(1, 10):
    arr[i].insert(0, 0)

for i in range(1, 10):
    for j in range(1, 10):
        # 행 체크
        if row[i][arr[i][j]] == 1:
            print("NO")
            exit()
        else:
            row[i][arr[i][j]] = 1

        # 열 체크
        if col[j][arr[i][j]]:
            print("NO")
            exit()
        else:
            col[j][arr[i][j]] = 1


        # 네모 체크
        tmp = 0
        if rect[(((i-1) // 3) * 3) + (((j - 1) // 3) + 1)][arr[i][j]] == 1:
            print("NO")
            exit()
        else:
            rect[(((i-1) // 3) * 3) + (((j - 1) // 3) + 1)][arr[i][j]] = 1


print("YES")