N = int(input())
time = []
for i in range(N):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda x: x[0])

# count = 0
# def checkRoomUse(assignmentsLeft, roomUse, count):
#     if len(assignmentsLeft) == 0:
#         return count
    
#     for assign in assignmentsLeft:
#         if roomUse[-1][1] <= assign:
#             checkRoomUse()

print(time)