import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

coins = [int(sys.stdin.readline().rstrip()) for i in range(N)]

# 문제에는 오름차순이라고 돼있는데 예시는 내림차순
# 오름차순이라고 가정하겠습니다

count = 0
for c in reversed(coins):
    count += K // c
    K = K % c

print(count)
