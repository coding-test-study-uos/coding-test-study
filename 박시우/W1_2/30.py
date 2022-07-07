numbers = [int(c) for c in input()]
numbers.sort(reverse=True)

multiple = []
max = ""
for n in numbers:
    max += str(n)
max = int(max)

i = 1
while True:
    if (i * 30) > max:
        break
    multiple.append(i * 30)
    i += 1
multiple.sort(reverse=True)

for i, m in enumerate(multiple):
    tempNumbers = numbers
    isPassed = True
    for c in str(m):
        if int(c) in tempNumbers:
            tempNumbers.remove(int(c))
        else:
            isPassed = False
            break
    if isPassed:
        print(m)
        break
    elif i == len(multiple) - 1:
        print(-1)