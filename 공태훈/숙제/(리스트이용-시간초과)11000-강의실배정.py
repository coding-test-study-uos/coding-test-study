
import sys
input = sys.stdin.readline

# 타임테이블을 만들어 입력된 시간에 강의가 있을 경우 해당시간에 +1을 한다
n = int(input())
nums = [list(map(int, input().split())) for i in range(n)]
nums.sort()
count = 1
end_times = []
end_times.append(nums[0][1])
for i in range(1, len(nums)):
    if min(end_times) <= nums[i][0]:
        end_times.remove(min(end_times))
        end_times.append(nums[i][1])

    else:
        end_times.append(nums[i][1])
        count += 1

print(count)
