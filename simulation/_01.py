N = int(input())

for i in range(N):
    _str = input().lower()
    _str_len = len(_str)

    # for j in range(_str_len // 2):
    #     if _str[j] != _str[_str_len -1 - j]:
    #                   _str[-1-j]
    #         print(f"#{i+1} NO")
    #         break
    # else:
    #     print(f"#{i+1} YES")

    # 위 방식도 좋지만 파이썬 기능을 활용하면 쉽게 해결가능하다.
    if _str == _str[::-1]:
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")


