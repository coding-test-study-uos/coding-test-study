# 리스트에서 min, append, remove는 많은 시간이 걸린다
# 우선순위큐에서 첫번째값이 min, push, pop 빠른 연산가능
import heapq
import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for i in range(n)]
nums.sort()
count = 1
# 끝나는 시간
end_times = []
heapq.heappush(end_times, nums[0][1])
for i in range(1, len(nums)):
    if end_times[0] <= nums[i][0]:
        heapq.heappop(end_times)
        heapq.heappush(end_times, nums[i][1])

    else:
        heapq.heappush(end_times, nums[i][1])
        count += 1

print(count)
