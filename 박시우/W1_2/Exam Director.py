import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split()) 

count = 0
for room in A:
    count += 1
    if (room - B) > 0:
        count += math.ceil((room - B) / C)
print(count)