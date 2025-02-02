"""
[시간복잡도] O(N**2)
    - 전체 지도에 대해 완전탐색 -> 25*25

* 연결되었다 = 상하좌우로 인접 -> 대각선은 연결된 것이 아니다.
** 단지의 수를 출력, 각 단지의 세대수를 오름차순으로 출력

소요시간 총 12분 내외
    - 구상: 3분
    - 구현: 9분
"""
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    num = 1
    while queue:
        x,y = queue.popleft()
        for f in range(4): # f of four
            nx = x+dx[f]
            ny = y+dy[f]
            if 0<=nx<N and 0<=ny<N and mp[nx][ny] and not visited[nx][ny]:
                num += 1 ## 세대 수 하나 추가
                queue.append((nx,ny)) ## 해당 단지 내에서 탐색할 다음 세대
                visited[nx][ny] = True
    return num

N = int(input())
mp = [list(map(int,input())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
answer_arr = list() ## 단지 내 세대수를 오름차순으로 정렬하기 위한 배열
cnt = 0 ## 단지 수

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(N):
    for y in range(N):
        if mp[x][y] == 1 and not visited[x][y]:
            answer_arr.append(bfs(x,y))
            cnt += 1


##############################################################

print(cnt)

answer_arr = sorted(answer_arr)
for i in answer_arr:
    print(i)
