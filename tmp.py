"""
* 중난도 스터디
[복잡도] O(N**2)
    - 30*30의 촬영 결과에 대해 완전 탐색

[구상]
    I: 촬영 결과의 크기 1<=N,M<=30
        - N개의 줄에 걸쳐 백신 놓기 전의 촬영 결과
        - N개의 줄에 걸쳐 백신 놓은 후의 촬영 결과
    O: 백신일 수 있다면 "YES", 그럴 수 없다면 "NO"


[고려사항]
    - 백신일 "수" 있다?
        - 백신은 4방으로 인접한 칸의 데이터 값이 같다면 퍼져나갈 수 있다
        => 백신 맞은 후의 촬영 결과를 바탕으로 bfs를 한다면
            - 접종 후 촬영 결과를 기준으로, 접종 전 촬영 결과와 다른 값을 갖는 영역의 갯수가 1개 이하여야 한다.
                - 즉, 다른 값을 갖는 영역의 수가 2 이상인 경우 "NO" 출력
                - 혹은 접종 전,후 촬영 결과의 bfs 호출 횟수를 나란히 비교하는 것도 가능

[테스트 케이스]
---
5 5
4 4 4 4 4
4 3 4 3 4
4 4 5 4 4
4 3 4 3 4
4 4 4 4 4
4 4 4 4 4
4 3 4 5 4
4 4 4 4 4
4 3 4 3 4
4 4 4 4 4
---

* 항체가 퍼졌던 칸들의 데이터 값은 모두 "어떤 동일한 값"으로 업데이트 된다.
** 원래의 데이터 값과 업데이트 된 데이터 값이 동일할 수도 있다.
"""
from collections import deque

def bfs(x,y):
    global diff_cnt
    is_different = False
    queue = deque()
    queue.append((x,y))
    v_a[x][y] = True    ## after 사진의 visited 배열
    if after[x][y] != before[x][y]:
        is_different = True
    while queue:
        x,y = queue.popleft()
        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]
            if 0<=nx<N and 0<=ny<M and not v_a[nx][ny] and after[x][y] == after[nx][ny]:
                queue.append((nx,ny))
                v_a[nx][ny] = True
                if after[nx][ny] != before[nx][ny]:
                    is_different = True             ## 이제부터 해당 bfs는 달라진 영역을 탐색하는 bfs가 된다.
    
    if is_different:                                ## 다른 영역을 탐색한 bfs 였다면, 다른 영역 수를 1 늘린다.
        diff_cnt += 1

def my_print(a):
    for x in a:
        print(x)
    print()

N, M = map(int,input().split())
before = [list(map(int,input().split())) for _ in range(N)]
after = [list(map(int,input().split())) for _ in range(N)]
v_a = [[False for _ in range(M)] for _ in range(N)]
global diff_cnt
diff_cnt = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(N):
    for y in range(M):
        if not v_a[x][y]:
            bfs(x,y)
        if diff_cnt >= 2:
            break
    if diff_cnt >= 2:
        break

if diff_cnt >= 2:           ## 접종 전/후의 값이 다른 영역의 수가 2 이상이라면
    print("NO")             
else:                       ## 접종 전/후의 값이 다른 영역의 수가 1 이하라면
    print("YES")

