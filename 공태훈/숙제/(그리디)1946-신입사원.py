# 입력의 양이 많다.
import sys
input = sys.stdin.readline

# 1, 첫번째 원소를 기준으로 오름차순정렬
# 2, 순회하며 현재 두번째 원소보다 작은 수를 뽑는다.
result = []
t = int(input())
for i in range(t):
    n = int(input())
    nums = [list(map(int, input().split())) for i in range(n)]
    nums.sort()
    # 두번째원소를 기준으로 크기가 작은것을 순서대로 뽑는다.
    now = nums[0][1]
    count = 1
    for i in nums:
        if i[1] < now:
            now = i[1]
            count += 1

    result.append(count)

for i in result:
    print(i)
