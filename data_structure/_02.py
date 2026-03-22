# ()(((()())(())()))(())
#                      1
# c: 0
# r: 17
s = input()

count = 0
res = 0

for i in range(len(s)):
    if s[i] == "(":
        count += 1

    elif s[i] == ")":
        if s[i - 1] == "(":
            count -= 1
            res += count
        elif s[i - 1] == ")":
            count -= 1
            res += 1

print(res)
