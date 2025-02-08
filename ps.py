"""
* 중난도 스터디
가장 큰 잘못: 백신일 수 있는 기준 자체에 틈이 있었던 것 같다.
    - 무조건 항체 맞은 자리에서 뻗어나갈 수 있을만큼 쭉 뻗어나가는 것으로 전제
        - 근데 애초에 백신이 아니면... 안 뻗어나갈 수도 있다.
    - 문제를 조금 더 간결하게 생각했으면 어땠을까?
        - 너무 막연하다고만 느끼니까 뭔가 더 큰게 있다고 생각하고 스스로 문제를 어렵게 만들었다.

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
                a 즉, 다른 값을 갖는 영역의 수가 2 이상인 경우 "NO" 출력
                b 혹은 접종 전,후 촬영 결과의 bfs 호출 횟수를 나란히 비교하는 것도 가능
    -> 위의 a,b 접근 둘 다 틀리길래 우선 하나라도 다른 지점 찾으면 해당 좌표 before 값을 after 값으로 바꿔주고, 직후에 before과 after이 다르다면 백신일 수 없는 것으로 판단

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
5 5
4 4 4 4 4
4 3 4 3 4
4 4 5 4 4
4 3 4 3 4
4 4 4 4 4
4 4 4 4 4
4 4 4 4 4
4 4 4 4 4
4 4 4 4 4
4 4 4 4 4
---
4 4
2 2 2 1
2 2 1 3
2 1 3 3
1 3 3 3
2 2 2 1
1 2 1 3
2 1 3 3
1 3 3 3
---
* 항체가 퍼졌던 칸들의 데이터 값은 모두 "어떤 동일한 값"으로 업데이트 된다.
** 원래의 데이터 값과 업데이트 된 데이터 값이 동일할 수도 있다.
"""
from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    v[x][y] = True    ## before 사진의 visited 배열
    started_value = before[x][y]    ## 항체가 타고 나갈 수 있는 값 (이 값과 같을 때만 퍼져나갈 수 있다)
    to_be = after[x][y]             ## 항체가 타고 나가 바꿔 놓을 값
    while queue:
        x,y = queue.popleft()
        before[x][y] = to_be        ## 항체 퍼져 나감
        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]
            if 0<=nx<N and 0<=ny<M and not v[nx][ny]:
                if before[nx][ny] == started_value: ## 퍼져나갈 수 있는 값이면 무조건 퍼져나간다 (아마 여기서 틀린 것 같은데, 퍼질 수 있는 값인데 안 나가도 백신이 아니다)
                    queue.append((nx,ny))
                    v[nx][ny] = True

def my_print(a):
    for x in a:
        print(x)
    print()

N, M = map(int,input().split())
before = [list(map(int,input().split())) for _ in range(N)]
after = [list(map(int,input().split())) for _ in range(N)]
v = [[False for _ in range(M)] for _ in range(N)]
possible = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(N):
    for y in range(M):
        if before[x][y] != after[x][y]:
            bfs(x,y)
            for x in range(N):
                for y in range(M):
                    if after[x][y] != before[x][y]: ## 항체 맞았는데도 다른 값이 남아있으면
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    if not possible:
        break

if not possible:
    print("NO")
if possible:
    print("YES")