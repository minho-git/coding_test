# 10
# 3 2 10 1 5 4 7 8 9 6

N = int(input())
arr = list(map(int, input().split()))
cur = 0
count = 0
res = ""

while True:
    if len(arr) != 1:
        if cur < arr[0] < arr[-1]:
            res += "L"
            count += 1
            cur = arr[0]
            arr.pop(0)

        elif arr[0] < cur < arr[-1]:
            res += "R"
            count += 1
            cur = arr[-1]
            arr.pop(-1)

        elif cur < arr[-1] < arr[0]:
            res += "R"
            count += 1
            cur = arr[-1]
            arr.pop(-1)

        elif arr[-1] < cur < arr[0]:
            res += "L"
            count += 1
            cur = arr[0]
            arr.pop(0)

        else:
            break

    else:
        if cur < arr[0]:
            res += "L"
            count += 1

        break

print(count)
print(res)



