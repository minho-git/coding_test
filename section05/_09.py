a = input()
b = input()

a_dict = {}
b_dict = {}
sh_dict = {}

# for x in a:
#     a_dict[x] = a_dict.get(x, 0) + 1
#
# for x in b:
#     b_dict[x] = b_dict.get(x, 0) + 1
#
# if a_dict == b_dict:
#     print("YES")
# else:
#     print("NO")

for x in a:
    sh_dict[x] = sh_dict.get(x, 0) + 1

for x in b:
    sh_dict[x] = sh_dict.get(x, 0) - 1

for x in sh_dict:
    if sh_dict[x] != 0:
        print("NO")
        break
else:
    print("YES")