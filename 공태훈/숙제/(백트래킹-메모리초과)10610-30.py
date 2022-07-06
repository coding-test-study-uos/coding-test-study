import sys
sys.setrecursionlimit(10**8)
def bt(depth):
    global answer
    if depth == max_depth:
        temp = int(''.join(map(str, result)))
        if temp % 30 == 0:
            answer = max(answer, temp)
    else:
        for i in range(len(n)):
            if visited[i] == 0:
                result[depth] = n[i]
                visited[i] = 1
                bt(depth+1)
                result[depth] = 0
                visited[i] = 0


# 숫자를 조합해서 30의 배수를 찾는다.
n = list(input())
max_depth = len(n)
visited = [0]*max_depth
result = [0]*max_depth
answer = 0
bt(0)
print(-1 if answer==0 else answer)
