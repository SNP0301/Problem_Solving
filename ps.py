"""
[복잡도] O(N**2)
    - 캠퍼스 최대 크기인 600*600에 대해 접근
        - 접근시마다 최대 4방향에 대해 탐색
"""
from collections import deque

def bfs(x,y):
    answer = 0
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for f in range(4): # f of four
            nx = x+ dx[f]
            ny = y+ dy[f]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if campus[nx][ny] == "O":
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif campus[nx][ny] == "P":
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    answer += 1
                elif campus[nx][ny] == "X":
                    visited[nx][ny] = True
                
    return answer



N, M = map(int,input().split())
campus = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for x in range(N):
    for y in range(M):
        if campus[x][y] == 'I':
            start_x = x
            start_y = y

answer = bfs(start_x, start_y)

if answer == 0:
    print("TT")
else:
    print(answer)

