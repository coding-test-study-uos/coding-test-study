# 어려워서 답지보고품
# 3의 배수임을 알기 위한 공식
# - 모든 자리수의 합이 3의 배수가 되면 그수는 3의 배수다


n = list(map(int, list(input())))

if 0 in n:
    if sum(n) % 3 == 0:
        n.sort(reverse=True)
        print(''.join(map(str, n)))
    else:
        print(-1)
else:
    print(-1)
