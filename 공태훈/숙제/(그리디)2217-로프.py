n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort(reverse=True)
# 가장 강한 로프부터 몇키로 들수있는지 검사하면서 최댓값을 저장한다.
# (가장 약한 로프)*(로프수) = > 현재로프로 들수있는 최대무게
result = 0
for i, v in enumerate(nums):
    result = max((i+1)*v, result)
print(result)
