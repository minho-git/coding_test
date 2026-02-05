n = int(input())
a = list(map(int, input().split()))
avg = int(sum(a)/n + 0.5)

min_dif = float('inf')
min_index = None

for index, value in enumerate(a):
    tmp = abs(value - avg)
    if min_dif > tmp:
        min_dif = tmp
        min_index = index

    elif min_dif == tmp:
        if value > a[min_index]:
            min_index = index

print(avg, min_index + 1)



