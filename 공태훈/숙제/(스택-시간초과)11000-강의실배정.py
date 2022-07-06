from collections import deque
# 끝시간-시작시간 기준으로 정렬후
# 겹치지 않는 수업은 하나의 강의실로한다
# 겹치지 않는 강의실 제거 후 다시 검색
n = int(input())
nums = [list(map(int, input().split())) for i in range(n)]
nums.sort(key=lambda x: (x[1]))
count = 0
while nums:
    count += 1
    remove_idx = deque()
    remove_idx.append(0)
    selected = []
    selected.append(nums[0][1])
    for i in range(1, len(nums)):
        if selected[-1] <= nums[i][0]:
            selected.append(nums[i][-1])
            remove_idx.append(i)

    # 안겹치는 강의실 삭제
    while remove_idx:
        # 입력한 순서역순으로 출력해야하므로 stack이용
        nums.pop(remove_idx.pop())


print(count)
