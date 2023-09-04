import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

w = -1
h = -1
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,1,-1,-1,0,1]

def dfs(x,y):
    visited[x][y] = True

    for i in range(8):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if nextX >= h or nextY >= w or nextX < 0 or nextY < 0:
            continue
        if visited[nextX][nextY] == False and graph[x][y] == graph[nextX][nextY]:
            dfs(nextX,nextY)



while w!=0 and h!= 0:
    w,h = map(int,input().split())
    if(w==0 and h==0):
        break
    graph = list()
    visited = [[False]*w for _ in range(h)]
    answer = 0

    for i in range(h):
        graph.append(input().split())

    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and graph[i][j] == '1':
                dfs(i,j)
                answer += 1
    print(answer)