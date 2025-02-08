"""
* 중난도 스터디
[복잡도] O(N)
    - 총 4개의 입력 명령을 수행
        - 명령당 최대 3<=R,C<=1_000 개의 배열 요소 탐색

[구상]
    I: 방의 크기 3<=R,C<=1_000, 장애물의 개수 0<=K<=1_000
        - 장애물의 위치 0<=br<=R-1, 0<=bc<=C-1
        - 로봇의 시작 위치 0<=sr<=R-1, 0<=sc<=C-1
    O: 로봇의 마지막 위치 r,c

[고려사항]
    - 로봇의 시작 위치에 장애물이 있는 경우는 없다.
    - 로봇은 지정한 방향을 일직선으로 움직인다 => 장애물을 만나거나, 벽을 만나거나, 방문했던 지역을 만날 때까지 이동
        - 장애물이 아니고, 벽도 아니고, 방문했던 지역도 아니어야 이동 가능
    - 사용자가 지정한 다음 방향이 없다면 맨 처음 방향으로 돌아가서 위의 과정을 반복
        - 4개의 명령이 끝나면 다시 명령[0]부터 시행
    - 로봇이 움직일 수 없을 경우 동작을 멈춘다.
        - 움직임을 for에서 관리하고, while 밑의 else에서 움직임 flag를 확인해 동작 멈춤 여부 결정

"""
from collections import defaultdict, deque

def my_print(a):
    for x in a:
        print(x)
    print()
R,C = map(int,input().split())
k = int(input())
room = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(k):
    br, bc = map(int,input().split())
    room[br][bc] = "X"
sx, sy = map(int,input().split())
room[sx][sy] = 1
cmd = list(map(int,input().split()))
move_dct = defaultdict(int)
not_moved_cnt = 0

#my_print(room)
for i in range(4):
    if cmd[i] == 1:
        move_dct[i] = (-1,0)
    elif cmd[i] == 2:
        move_dct[i] = (1,0)
    elif cmd[i] == 3:
        move_dct[i] = (0,-1)
    elif cmd[i] == 4:
        move_dct[i] = (0,1)


d = 0
while not_moved_cnt < 4:
    cnt = 1
    moved= False
    while True:
        nx = sx + move_dct[d][0]
        ny = sy + move_dct[d][1]
        if 0<=nx<R and 0<=ny<C and room[nx][ny] == 0:
            #print(sx,sy,"---->",nx,ny,move_dct[d])
            room[nx][ny] = 1
            #my_print(room)
            sx = nx
            sy = ny
            moved = True
            not_moved_cnt = 0

        else:
            d = (d+1)%4         ## 움직임 방향 바꿔주기
            break
    if not moved:
        not_moved_cnt += 1

    
print(sx,sy)