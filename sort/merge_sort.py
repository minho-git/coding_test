# 4 5 1 3 2
array = list(map(int, input().split()))

def merge_sort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2

        merge_sort(lt, mid)
        merge_sort(mid + 1,rt)

        tmp = []

        pos1 = lt
        pos2 = mid + 1

        while pos1 <= mid and pos2 <= rt:
            if array[pos1] < array[pos2]:
                tmp.append(array[pos1])
                pos1 += 1
            else:
                tmp.append(array[pos2])
                pos2 += 1

        if pos1 <= mid:
            tmp += array[pos1: mid+1]
        elif pos2 <= rt:
            tmp += array[pos2: rt+1]


        array[lt: rt + 1] = tmp

merge_sort(0, len(array)-1)

print(array)

