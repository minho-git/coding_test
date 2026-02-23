N, M = map(int, input().split())
graph = [0] * M
res = 0

# 조합은 선택된것 제외.
# 목표: 중복된 조합(예: (1, 2)와 (2, 1))을 제거하고 싶다.
# 전략: "오름차순으로만 뽑자"는 규칙을 세운다. (순서를 강제함)
# 구현: start 변수를 도입하여, 다음 단계에서는 "이전 값보다 큰 값(i+1)부터" 탐색하도록 만든다.

def dfs(level, start):
    global res

    if level == M:
        for x in graph:
            print(x, end=" ")
        print()
        res += 1

    else:
        for i in range(start, N+1):
            graph[level] = i
            dfs(level+1, i + 1)

dfs(0, 1)
print(res)