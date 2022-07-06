n = int(input())
times = [list(map(int, input().split())) for i in range(n)]
# 끝시간-시작시간순으로 정렬후
# 현재회의의 끝시간보다 늦은 시작시간을 가진 첫번째 회의를 선택
times.sort(key=lambda x: (x[1], x[0]))
selected_conf = []
# 첫번째 원소는 무조건 포함이 된다
selected_conf.append(times[0])
for i in range(1, len(times)):
    # 선택된 회의의 마지막원소의 끝시간보다 현재회의의 시작시간이 크같경우
    if selected_conf[-1][1] <= times[i][0]:
        selected_conf.append(times[i])

print(len(selected_conf))


##
# 1. 그리디라는 점을 떠올리기
# 2. 첫번째 원소가 무조건 포함된다는 점
