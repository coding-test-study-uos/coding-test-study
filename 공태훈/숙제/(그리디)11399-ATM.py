# 돈을 빠르게 뽑는사람먼저 뽑게하면 최소
n = int(input())
nums = list(map(int, input().split()))
# 돈뽑는시간이 빠른 사람순으로 정렬
nums.sort()
# 누적합 리스트
for i in range(1, len(nums)):
    nums[i] += nums[i-1]

answer = 0
# 맨앞사람부터 현재사람까지 걸린시간을 더함(누적합이용)
for i in nums:
    answer += i

print(answer)
