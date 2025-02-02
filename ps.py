"""
[시간복잡도] O(N**2)
    - 전체 사람에 대해 완전탐색하므로, 100*100

* 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
** 칸을 셀 때는 시작 위치와 도착 위치도 포함한다.

소요시간 총 17분 내외
    - 구상: 5분
    - 구현: 12분
"""
from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    score_arr[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for f in range(4): ## f of four
            nx = x + dx[f]
            ny = y + dy[f]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny] != 0:
                score_arr[nx][ny] = score_arr[x][y]+1
                queue.append((nx,ny))
                visited[nx][ny] = True
                

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
score_arr = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

bfs(0,0)

print(score_arr[N-1][M-1])
