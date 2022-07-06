from itertools import permutations

# 숫자를 조합해서 30의 배수를 찾는다.
n = list(input())
answer = 0
for i in list(permutations(n, len(n))):
    temp = int(''.join(i))
    if temp % 30 == 0:
        answer = max(temp, answer)

print(answer)
