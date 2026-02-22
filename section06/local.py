a = [1, 2, 3]

# a = <- 지역 변수를 만들겠다는 의미
def dfs():
    global a

    a += [1]
    print(a)

dfs()
print(a)