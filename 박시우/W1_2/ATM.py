N = int(input())
P = [time for time in map(int,input().split())]
P.sort()

sum = 0
sumIter = 0
for i in range(len(P)):
    sumIter += P[i]
    sum += sumIter

print(sum)