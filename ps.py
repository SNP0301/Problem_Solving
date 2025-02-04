"""
[복잡도] O(N**2)
    - 1000*1000 상자에 대해 완전탐색
    - BFS 시행 횟수는 주어진 익은 토마토(초기값 1)의 갯수와 동일

[구상]
    - 변수
        - arr[][]: 익은 토마토, 안 익은 토마토, 벽
        - visited[][]: 방문 여부 결정
        - queue(): BFS 대상 좌표 저장
        - at_least_one: 모든 토마토가 익어있는 경우와 그렇지 않은 경우를 구분하는 boolean
        - is_possible: 모든 토마토가 익지는 못하는 경우임을 나타내는 boolean
        - dx[], dy[]: 4방향 탐색을 위한 방향 배열
        - mx: 토마토가 익는 데에 걸리는 최소 시간
    - 2차원 배열을 입력 받고, 이중 for 문으로 이미 익은 토마토의 위치를 탐색 -> 찾은 토마토의 위치는 queue에 저장.
        - 예제 입력 3과 같이, 2개 이상의 익은 토마토가 있을 때 다른 문제처럼 BFS를 한번만 수행하면
          최단거리가 갱신되지 않는 문제 발생
    - BFS 수행 내용 - 4방향 탐색
        - 탐색 칸의 4방향 인접 칸 중 0인 칸을 찾으면 탐색 칸의 값 + 1을 저장
            - 해당 인접칸을 queue에 push
            - 해당 인접칸 visited 표시
            - 저장될 때부터 모든 토마토가 익어있는 경우와 그렇지 않은 경우를 구분하기 위해 at_least_one = True로 갱신
        - 탐색 칸의 4방향 인접 칸 중 0이 아니지만 탐색 칸의 값 + 1 보다 큰 값을 가지고 있으면 최단거리 갱신
            - 해당 분기는 이미 다른 bfs 실행에서 해당 칸을 방문했던 경우에 발생 -> visited 갱신 필요 x

* 저장될 때부터 모든 토마토가 익어있는 상태면 0을 출력
** 토마토가 모두 익지는 못하는 상황이면 -1 출력
"""
def bfs(x,y):
    visited[x][y] = True
    global at_least_one
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for f in range(4): ## f of four
            nx = x + dx[f]
            ny = y + dy[f]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    at_least_one = True
                elif arr[nx][ny] != 1 and arr[nx][ny] != -1:
                    if arr[nx][ny] > arr[x][y] + 1:
                        arr[nx][ny] = arr[x][y] + 1
        
from collections import deque

M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

at_least_one = False ## 모든 토마토가 익어있다고 선언 -> 하나라도 새로 익으면 True로 갱신
mx = -2
is_possible = True ##
queue = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            queue.append((x,y))
if queue:
    sx, sy = queue.popleft()
    bfs(sx,sy)

for x in range(N):
    for y in range(M):
        if arr[x][y] == 0:
            is_possible = False
        if arr[x][y] > mx:
            mx = arr[x][y]


if not is_possible:
    print(-1)
elif is_possible:
    if not at_least_one:
        print(0)
    elif at_least_one:
        print(mx-1)
