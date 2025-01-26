"""
[실수한 것]
- ny 선언할 때 [x] 자리에 [y]가 들어감
"""

N = int(input())
game_arr = [list(map(int,input().split())) for _ in range(N)]
score_arr = [[0 for _ in range(N)] for _ in range(N)]

dx = [0,1]
dy = [1,0]
score_arr[0][0] = 1
for x in range(N):
    for y in range(N):
        for d in range(2):
            nx = x + dx[d]*game_arr[x][y]
            ny = y + dy[d]*game_arr[x][y]
            if 0 <= nx < N and 0 <= ny < N:
                if game_arr[x][y] != 0:
                    #print("from [%d, %d], can go to [%d, %d] with %d power"%(x,y,nx,ny,game_arr[x][y]))
                    score_arr[nx][ny] += score_arr[x][y]
                elif game_arr[x][y] == 0:
                    continue

print(score_arr[N-1][N-1])
