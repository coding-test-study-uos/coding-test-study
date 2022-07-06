# 가장 높은 값에 다른 값을 을 더한 합
n = input()
nums = list(map(int, input().split()))
nums.sort(reverse=True)
# 누적합 리스트
# 최댓값과 자신을 더한 합 리스트
for i in range(1, len(nums)):
    nums[i] += nums[0]

#최댓값 제거
print(sum(nums[1:]))
