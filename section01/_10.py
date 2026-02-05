# 2차원 리스트 생성과 접근


# 1차원 리스트 생성
# a = [0] * 3
# print(a)

a = [[0] * 3 for _ in range(3)]
a[0][1] = 1
a[1][1] = 2
# print(a)

# 2차원 리스트를 표 형태로 보기
for x in a:
    print(x)

# 일일히 확인
for x in a:
    for j in x:
        print(j, end=" ")
    print()

