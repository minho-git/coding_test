N = int(input())

dic = {}
for i in range(N):
    dic[input()] = 0

for i in range(N-1):
    dic[input()] = 1

for key, value in dic.items():
    if value == 0:
        print(key)
        break
