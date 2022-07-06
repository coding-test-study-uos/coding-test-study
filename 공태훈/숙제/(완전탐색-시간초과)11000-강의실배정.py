import sys
from collections import deque
input = sys.stdin.readline
# 끝시간-시작시간 기준으로 정렬후
# 겹치지 않는 수업은 하나의 강의실로한다
# 겹치지 않는 강의실 제거 후 다시 검색
n = int(input())
nums = [list(map(int, input().split())) for i in range(n)]
nums.sort(key=lambda x: (x[1]))
count = 0
remove_idx = set()


for i in range(0, len(nums)):
    if i not in remove_idx:
        selected = []
        selected.append(nums[i][1])
        remove_idx.add(i)
        for j in range(i+1, len(nums)):
            if j not in remove_idx and selected[-1] <= nums[j][0]:
                selected.append(nums[j][1])
                remove_idx.add(1)
        count += 1


print(count)
