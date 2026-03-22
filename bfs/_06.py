s = input()
arr = list(map(int, s))
N = len(arr)
res = 0
def dfs(level, result):
    global res

    if level == N:
        print(result)
        res += 1

    # 0은 혼자 다니지 못한다.
    elif arr[level] == 0:
        return

    else:
        dfs(level+1, result + chr(arr[level] + 64))

        if level != N-1:
            tmp = arr[level] * 10 + arr[level + 1]
            if tmp < 27:
                dfs(level + 2, result + chr(tmp + 64))

dfs(0, "")
print(res)

# 1556101021201310516411203212132