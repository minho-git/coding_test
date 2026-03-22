_str = input()
tmp = ""

for x in _str:
    if x.isdigit():
        tmp += x

    # 이 풀이도 가능
    # res = 0
    # res = res * 10 + int(x)

answer = int(tmp)
count = 0

# 약수 구하기
# 아래 방식은 시간복잡도 O(n)이 걸린다.
# 문제에서 자연수의 크기가 1억까지 가능하다했으므로, 약 1초가 걸린다.
# 시간복잡보 초과 가능성이 존재.
# 제곱근까지만 검사하자.

# for i in range(1, answer + 1):
#     if answer % i == 0:
#         count+=1

for i in range(1, int(answer**(1/2))+1):
    if answer % i == 0:
        count += 1
        if i * i != answer: # 제곱수가 아닐때는 상대편 약수까지 더해줘야한다.
            count += 1

print(answer)
print(count)