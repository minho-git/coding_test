# ▣ 입력예제 1
# 5276823 3

# ▣ 출력예제 1
# 7823

arr, N = map(int,input().split())
stk = []
res = []

# 일단 10으로 나눈 나머지로 스택에 담아.
while arr > 0:
    stk.append(arr%10)
    arr //= 10

# 하나씩 꺼내면서 자기보다 작은게 스택이 있으면 빼내(arr.pop(-1)). 그리고 count 증가시켜.
for i in range(len(stk)):
    cur = stk.pop()

    for j in range(len(res)):
        if N == 0:
            break

        if cur > res[-1]:
            res.pop()
            N -= 1
        else:
            break

    res.append(cur)


for i in range(N):
    res.pop()

# 이렇게 반복하다가 count == N 이랑 같아지면 끝!
# 마지막에 남은 카운터만큼 끝에서 제거하기!

for x in res:
    print(x, end="")
