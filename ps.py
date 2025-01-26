"""
* 100을 넘지 않는 음이 아닌 정수만큼 K,Q,P가 주어진다
** 한 칸에는 하나의 말만 놓인다
*** Q는 K,P에게 각각 막힌다
"""

################################################################
n,m = map(int,input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
q_list = list(map(int,input().split()))
k_list = list(map(int,input().split()))
p_list = list(map(int,input().split()))

q_dx = [-1,0,1,1,1,0,-1,-1]
q_dy = [1,1,1,0,-1,-1,-1,0]

k_dx = [-2,-1,1,2,2,1,-1,-2]
k_dy = [1,2,2,1,-1,-2,-2,-1]

for i in range(1,len(q_list)-1,2):
    board[q_list[i]-1][q_list[i+1]-1] = "Q"

for i in range(1,len(k_list)-1,2):
    board[k_list[i]-1][k_list[i+1]-1] = "K"

for i in range(1,len(p_list)-1,2):
    board[p_list[i]-1][p_list[i+1]-1] = "P"

for x in range(n):
    for y in range(m):
        if board[x][y] == "Q":
            for e in range(8): ## e of eight
                cnt = 1
                is_done = False
                while not is_done:
                    nx = x + q_dx[e] * cnt
                    ny = y + q_dy[e] * cnt
                    ##print(nx,ny)
                    if (0<=nx<n and 0<=ny<m):
                        if board[nx][ny] == 0 or board[nx][ny] == 1:
                            board[nx][ny] = 1
                            cnt += 1
                        elif board[nx][ny] == "K" or board[nx][ny] == "P" or board[nx][ny] == "Q":
                            is_done = True
                            break
                    else:
                        is_done = True
        elif board[x][y] == "K":
            for e in range(8): ## e of eight
                nx = x + k_dx[e]
                ny = y + k_dy[e]
                if (0<=nx<n and 0<=ny<m):
                    if board[nx][ny] == 0 or board[nx][ny] == 1:
                        board[nx][ny] = 1
                    else:
                        continue
        else:
            continue           


################################################################
for i in board:
    answer += i.count(0)
print(answer)