# 문자열과 내장함수
msg = "It is Time"
print(msg.upper()) # 원본은 그대로
print(msg.lower())
print(msg)
print()

tmp = msg.upper()
print(tmp)
print(tmp.find('T')) # 처음으로 발견된 T의 인덱스 출력
print(tmp.count('T'))
print()

print(msg)
print(msg[:2])
print(len(msg))
print()

# 문자열 1개씩 접근하기
for i in range(len(msg)):
    print(msg[i], end=" ")
print()
print()

for x in msg:
    print(x, end=" ")
print()
print()

for x in msg:
    if x.isupper():
        print(x, end=" ")
print()
print()

# 공백 제거
for x in msg:
    if x.isalpha():
        print(x, end="")
print()
print()

print(msg.replace(" ", ""))
print()

tmp = "AZ"
for x in tmp:
    print(ord(x), end=" ")
print()

tmp = "az"
for x in tmp:
    print(ord(x), end=" ") # ascii to num
print()

tmp = [65, 90]
for x in tmp:
    print(chr(x), end=" ") # num to ascii



