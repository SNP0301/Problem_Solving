"""
[복잡도] O(N**2)
    - 10*10의 보드칸에서 BFS

[구상]
    I: 사다리의 수 1<=N<=15, 뱀의 수 1<=M<=15
        - N개의 줄에 걸쳐 사다리 정보 x<y -> x에 도착하면 y번 칸으로 이동
        - M개의 줄에 걸쳐 뱀의 정보 u>v -> u에 도착하면 v번 칸으로 이동
    O: 100번 칸에 도착하기 위해 주사위를 돌릴 수 있는 수
    - 10*10이라고는 하지만 4방향 탐색이 아니다.
        => 주사위가 6까지 있으니, 현재 위치가 x 일 때 x+1부터 x+6까지 탐색한다.
    - 방문 안 했으면 방문하고, 그 칸에 사다리/뱀이 있었다면 사다리/뱀 타고 간 칸에도 같은 이동 횟수를 넣는다. (+1 하면 안된다)
    - 방문 했는데 지금 주려는 번호보다 더 큰 값이 적혀있으면 이동 횟수를 갱신해주고, append

[테스트 케이스]
---
1 1
3 98
2 99

ans = 2
---
1 1
2 51
3 1

ans = 10
---
1 1
1 2
4 3


* 1번 칸과 100번 칸은 뱀/사다리의 시작 또는 끝이 아니다.
** 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있다. 동시에 두가지를 모두 가지는 경우는 없다.
*** 무조건 100번 칸에 도착할 수 있는 입력만 주어진다.
"""
from collections import defaultdict, deque

N, M = map(int,input().split())
board = [0 for _ in range(101)]   ## 1번칸부터 100번칸
v = [False for _ in range(101)]   ## 1번칸부터 100번칸
ladder_dct = defaultdict(int)       ## ladder_dct[시작 칸] = 도착 칸
snake_dct = defaultdict(int)        ## snake_dct[시작 칸] = 도착 칸

for _ in range(N):                  ## 사다리 정보 저장
    s,e = map(int,input().split())
    ladder_dct[s] = e

for _ in range(M):                  ## 뱀 정보 저장
    s,e = map(int,input().split())
    snake_dct[s] = e

queue = deque()
queue.append(1)
v[1] = True

while queue:
    x = queue.popleft()
    cur = board[x]

    for s in range(1,7):              ## s of six
        if 1<=x+s<=100:
            if x+s in ladder_dct:
                if not v[ladder_dct[x+s]]:          ## A-1) 주사위 굴려서 나온 칸에 사다리가 있으면
                    board[ladder_dct[x+s]] = cur + 1
                    v[ladder_dct[x+s]] = True
                    queue.append(ladder_dct[x+s])
                elif v[ladder_dct[x+s]] and board[ladder_dct[x+s]] > cur + 1:
                    board[ladder_dct[x+s]] = cur + 1
                    queue.append(ladder_dct[x+s])   ## + 다시 탐색


            elif x+s in snake_dct:                  ## A-2) 주사위 굴려서 나온 칸에 뱀이 있으면
                if not v[snake_dct[x+s]]:       
                    board[snake_dct[x+s]] = cur + 1
                    v[snake_dct[x+s]] = True
                    queue.append(snake_dct[x+s])
                elif v[snake_dct[x+s]] and board[snake_dct[x+s]] > cur + 1:
                    board[snake_dct[x+s]] = cur + 1
                    queue.append(snake_dct[x+s])    ## + 다시 탐색
            else:                                   ## A-3) 주사위 굴려서 나온 칸에 아무 것도 없으면
                if not v[x+s]:
                    board[x+s] = cur + 1
                    queue.append(x+s)
                    v[x+s] = True
                elif v[x+s] and board[x+s] > cur + 1:
                    board[x+s] = cur + 1
                    queue.append(x+s)







    
print(board[100])

"""
for i in range(10):
    for j in range(10):
        print(board[i*10+j+1],end=" ")
    print()
"""