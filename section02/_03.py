N, K = map(int, input().split())
numbers = list(map(int, input().split()))
answer = set()

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            answer.add(numbers[i]+ numbers[j] + numbers[k])

answer = sorted(answer, reverse=True)
print(answer[K-1])



