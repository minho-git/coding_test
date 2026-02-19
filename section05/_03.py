# *, / : 이건 스택에 들어있는 *, / 빼줘야 한다.
# +, - : 이걸 만났을때 스택에서 다 빼준다. 왜냐하면 우선순위가 가장 낮고, 왼쪽에 있는게 먼저 실행되어야 하기 때문이다.

# 스택 상단이 먼저 실행되니깐 자기보다 먼저 실행되어야하는 것을 빼준다고 생각하자.
s = input()
stack = []
res = ""

for x in s:
    if x.isdigit():
        res += x
    else:
        if x == '(':
            stack.append('(')

        elif x in ["*", "/"]:
            while stack and stack[-1] in ["*", "/"]:
                res += stack.pop()
            stack.append(x)

        elif x in ["+", "-"]:
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)

        elif x == ")":
            while stack and stack[-1] != '(':
                res += stack.pop()

            stack.pop()

while stack:
    res += stack.pop()

print(res)