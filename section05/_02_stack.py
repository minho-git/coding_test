s = input()

stack = []
res = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append("(")

    elif s[i] == ")":
        stack.pop()

        if s[i-1] == ")":
            res += 1
        else:
            res += len(stack)

print(res)
