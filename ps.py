"""
* 어디서 틀린거지?

T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    visited= [[False for _ in range(M)] for _ in range(N)]
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    answer = 0

    for _ in range(K):
        y,x = map(int,input().split())
        field[x][y] = 1

    for x in range(N):
        for y in range(M):
            if field[x][y] == 1 and not visited[x][y]:
                next_search = [[x,y]]
                visited[x][y] = True
                while next_search:
                    #print("before: ",next_search)
                    x = next_search[0][0]
                    y = next_search[0][1]
                    next_search.pop(0)
                    for f in range(4): ## t of two
                        nx = x+dx[f]
                        ny = y+dy[f]
                        if 0<=nx<N and 0<=ny<M and field[nx][ny] == 1 and not visited[nx][ny]:
                                next_search.append([nx,ny])
                                visited[nx][ny]= True
                    #print("after: ",next_search)
                answer += 1
    print(answer)
"""




T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = [(x,y)]
    field[x][y] = 0
    while queue:
        x,y = queue.pop()

        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]

            if 0<=nx<N and 0<=ny<M:
                if field[nx][ny] == 1:
                    queue.append((nx,ny))
                    field[nx][ny] = 0
        

for _ in range(T):
    M,N,K = map(int,input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0

    for _ in range(K):
        y,x = map(int,input().split())
        field[x][y] = 1

    for x in range(N):
        for y in range(M):
            if field[x][y] == 1:
                BFS(x,y)
                answer += 1
    print(answer)