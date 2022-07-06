n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
coins.sort(reverse=True)
# 가장 비싼 동전를 먼저 쓴다.
answer = 0
for i in coins:
    answer += k//i
    k = k % i

print(answer)
