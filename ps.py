"""
[복잡도] O(N**2)
    - 500*500의 도화지에 대해 완전탐색

[구상]
    - 그림의 수 = BFS 수행횟수
    - 그림 넓이의 최대값 = BFS 실행 결과 중 최대값 -> BFS 끝날 때마다 max()로 갱신

    
* 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
* 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
* 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
* 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
* 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
[] 문제 읽기 -> [] I/O 확인 -> [] 제약조건/특이사항 확인 -> [] 구상 -> [] 복잡도 계산 -> [] 손 구현 -> [] 구현 -> [] 오픈테케 -> []히든테케
"""
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    area = 1

    while queue:
        x,y = queue.popleft()
        for f in range(4): ## f of four
            nx = x + dx[f]
            ny = y + dy[f]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                area += 1
    return area
    
N, M = map(int,input().split())
visited = [[False for _ in range(M)] for _ in range(N)]
arr = [list(map(int,input().split())) for _ in range(N)]
answer = 0
mx = -1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(N):
    for y in range(M):
        if arr[x][y] == 1 and not visited[x][y]:
            area = bfs(x,y) ## area는 해당 그림의 넓이를 받는다
            mx = max(mx,area) ## 최대 넓이 갱신
            answer += 1 ## 그림의 갯수 하나 추가
if answer == 0:
    mx = 0
print(answer)
print(mx)