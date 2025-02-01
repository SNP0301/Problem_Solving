"""
[복잡도] O(N^2)
    - 1000*1000 arr의 elem에 대해 4개의 근접 elem 탐색/연산
    - 시간 제한 1초인거 보고 어떻게 생각해야하지? 가능?불가능?
[구상]
    - input은 mp에 저장
    - 정답은 answer에 저장 -> 각 요소는 1000*1000+1로 선언
    - v에 방문 여부 저장
    - 탐색 시작
        - "2"인 곳에서 시작, cur = 0
        - 0<=nx<X, 0<=ny<Y, not v[nx][ny] 일 때
            - mp[nx][ny] != 0 이면 이동 가능
                - mp[x][y]+1한 값을 answr[nx][ny]에 저장, deque에 [nx][ny] append
            - mp[nx][ny] == 0 이면 이동 불가능
                - visited만 변경 (answer[x][y] 초기값은 0이므로 값 변경 필요 x)
    - 탐색 종료
        - not v[x][y]인 곳이 있으면 answer[x][y] = -1로 변경
"""
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    v[x][y] = True
    while queue:
        x,y = queue.popleft()
        for f in range(4): # f of four
            nx = x+dx[f]
            ny = y+dy[f]
            if 0<=nx<N and 0<=ny<M and not v[nx][ny]:
                if mp[nx][ny] != 0:
                    answer[nx][ny] = answer[x][y] + 1
                    v[nx][ny] = True
                    queue.append((nx,ny))
                elif mp[nx][ny] == 0:
                    v[nx][ny] = True

def my_print(a):
    for x in a:
        print(x)
    print()

N, M = map(int,input().split())
mp = [list(map(int,input().split())) for _ in range(N)]
v = [[False for _ in range(M)] for _ in range(N)]
answer = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for x in range(N):
    for y in range(M):
        if mp[x][y] == 2:
            start_x = x
            start_y = y

#print(start_x,start_y)

bfs(start_x, start_y)


for x in range(N):
    for y in range(M):
        if v[x][y] == 0 and mp[x][y] != 0:
            print(-1,end=" ")
        else:
            print(answer[x][y],end=" ")
    print()
