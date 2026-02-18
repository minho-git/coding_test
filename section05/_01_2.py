num, M = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
    while stack and M > 0 and stack[-1] < x:
        stack.pop()
        M -= 1

    stack.append(x)

if M != 0:
    stack = stack[:-M]

# for x in stack:
#     print(x, end="")

# join의 역할:
# "".join(리스트)는 리스트 안의 문자열 요소들을 ""(빈 문자열)로 이어 붙여서 하나의 큰 문자열로 만들어주는 함수입니다.
print("".join(map(str, stack)))