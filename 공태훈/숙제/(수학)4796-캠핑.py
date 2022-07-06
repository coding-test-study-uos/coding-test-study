def calCampDay(l, p, v):
    temp = l*(v//p)
    temp2 = v % p if v % p < l else l
    return str(temp+temp2)


test_count = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0:
        break
    print("Case "+str(test_count)+": " + calCampDay(l, p, v))
    test_count += 1
