str1 = input()
str2 = input()

a = [0] * 52
b = [0] * 52

for x in str1:
    if x.isupper():
        a[ord(x) - ord("A")] += 1
    else:
        a[ord(x) - ord("a") + 26] += 1


for x in str2:
    if x.isupper():
        b[ord(x) - ord("A")] += 1
    else:
        b[ord(x) - ord("a") + 26] += 1

if a != b:
    print("NO")
else:
    print("YES")
