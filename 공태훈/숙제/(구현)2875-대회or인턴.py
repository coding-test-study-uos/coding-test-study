
import math
woman, man, k = map(int, input().split())
team = 0

# 일단 되는되로 팀만들기
while True:
    if man >= 1 and woman >= 2:
        man -= 1
        woman -= 2
        team += 1
    else:
        break
# 팀만들고 남은 인원을 인턴쉽에 추가
k -= woman+man
# 남은 인원들로 인턴쉽인원이 찼으면 team수 반환
if k <= 0:
    print(team)

# 남은 인원으로도 부족할경우 팀쪼개기
else:

    # 필요한 인원/3의 올림을 하여 쪼갤 팀의 수결정
    team -= math.ceil(k/3)

    # 팀의수가 음수가 될경우 만들 수 없음
    if team < 0:
        print(0)
    else:
        print(team)
