N = int(input())
arr = list(map(int, input().split()))
last = 0
res = ""
s = 0
e = N-1

while s <= e:
    tmp = []
    if last < arr[s]:
        tmp.append((arr[s], "L"))

    if last < arr[e]:
        tmp.append((arr[e], "R"))

    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]

        if tmp[0][1] == "L":
            s += 1
        else:
            e -= 1

print(len(res))
print(res)

# "현재의 최적 선택(작은 값 선택)이 전체의 최적해(최장 길이)를 보장한다"는 그리디의 논리입니다.