# 352+*9-
# 12

s = list(input())
stack = []
for x in s:
    if x.isdecimal():
        stack.append(int(x))

    else:
        num2 = stack.pop()
        num1 = stack.pop()

        if x == "+":
            stack.append(num1 + num2)
        elif x == "-":
            stack.append(num1 - num2)
        elif x == "*":
            stack.append(num1 * num2)
        elif x == "/":
            stack.append(num1 // num2)

print(stack[0])
