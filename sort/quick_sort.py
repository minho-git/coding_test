# 4 5 1 3 2
array = list(map(int, input().split()))

def quick_sort(lt, rt):

    if lt >= rt:
        return

    pivot = array[rt]

    pos = lt

    for i in range(lt, rt):
        if pivot > array[i]:
            array[pos], array[i] = array[i], array[pos]
            pos += 1


    array[pos], array[rt] = array[rt], array[pos]

    quick_sort(lt, pos-1)
    quick_sort(pos+1, rt)

quick_sort(0, len(array) - 1)

print(array)

