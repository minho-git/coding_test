# arr = [i for i in range(0, 21)]
arr = list(range(21))

for _ in range(10): # 의미 없는건 _ 로 설정

    ai, bi = map(int, input().split())

    # for j in range((bi - ai + 1) // 2):
    #     arr[ai + j], arr[bi - j] = arr[bi - j], arr[ai + j]

    arr[ai:bi+1] = arr[bi:ai-1:-1]
    # arr[ai:bi+1] = arr[ai:bi+1][::-1]


for i in range(1,21):
    print(arr[i], end=" ")

