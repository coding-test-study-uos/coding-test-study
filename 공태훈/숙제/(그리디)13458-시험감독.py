import math
n = int(input())  # 시험장수
peoples = list(map(int, input().split()))  # 시험장별 응시생수
b, c = map(int, input().split())  # 총갑독 감시능력b, 부감독c
answer = 0


# 최소 총감독관 교실당 하나배정
answer += n  # 교실에 총감독관 하나씩배정
for i in range(len(peoples)):
    peoples[i] -= b  # 감시해야하는 학생수 줄이기

# 남은 감시인원 배정
for i in range(len(peoples)):
    if peoples[i] > 0:
        answer += math.ceil(peoples[i]/c)

print(answer)

########
# 총감독관을 배치할 때 남은 감시해야하는 학생수가 음수가 되는 예외
########
