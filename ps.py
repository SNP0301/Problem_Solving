import sys
input = sys.stdin.readline

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = [(x,y)]
    matrix[x][y] = 0
    while queue:
        x,y = queue.pop()

        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]

            if nextX < 0 or nextX >= M or nextY < 0 or nextY >= N:
                continue

            if matrix[nextX][nextY] == 1:
                queue.append((nextX, nextY))
                matrix[nextX][nextY] = 0
        

for _ in range(T):
    M,N,K = map(int,input().split())
    matrix = [[0]*(N) for _ in range(M)]
    cnt = 0

    for _ in range(K):
        x,y = map(int,input().split())
        matrix[x][y] = 1
    
    for a in range(M):
        for b in range(N):
            if matrix[a][b] == 1:
                BFS(a,b)
                cnt += 1

    print(cnt)
