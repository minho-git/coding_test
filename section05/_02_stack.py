s = input()

stack = []
res = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append("(")

    elif s[i] == ")":
        stack.pop() # 무조건 하나 빼줘야 한다.

        if s[i-1] == ")":
            res += 1
        else:
            res += len(stack)

print(res)
