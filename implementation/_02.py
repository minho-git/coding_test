T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())

    original = list(map(int, input().split()))
    transformed = original[s-1:e]

    transformed.sort()
    result = transformed.pop(k-1)
    print(f"#{i+1} {result}")






