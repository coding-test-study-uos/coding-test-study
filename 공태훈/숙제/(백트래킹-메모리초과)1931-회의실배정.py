import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def bt(depth, end):
    global answer
    answer = max(answer, len(result))
    for i in range(n):
        # 회의의 시작히간이 현재 끝시간보다 크거나 같을 때
        if times[i][0] >= end and visited[i] == 0:
            visited[i] = 1
            result.append(i)
            # 끝시간을 저장하여 백트래킹
            bt(depth+1, times[i][1])
            visited[i] = 0
            result.pop()


if __name__ == '__main__':
    n = int(input())
    times = [list(map(int, input().split())) for i in range(n)]
    visited = [0]*(n)
    result = []
    answer = 0
    # 시작시간-끝시간을 기준으로 정렬
    times.sort()
    bt(1, 0)
    print(answer)
