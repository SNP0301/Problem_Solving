import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

t = int(input())

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]


def dfs(x,y):
    global cnt
    global cntArr

    visited[x][y] = True

    for j in range(8):
        nextX = x + dx[j]
        nextY = y + dy[j]

        if nextX < 0 or nextY < 0 or nextX >= i or nextY >= i:
            continue
        if x == endX and y == endY:
            cntArr.append(cnt)
            cnt = 0
        if visited[nextX][nextY] == False:
            dfs(nextX, nextY)
            cnt += 1
            
            

for _ in range(t):
    i = int(input())
    cnt = 0
    cntArr = list()
    graph = [[0]*i for _ in range(i)]
    visited = [[False]*i for _ in range(i)]
    startX, startY = map(int,input().split())
    endX, endY = map(int,input().split())

    dfs(startX, startY)
    print(cntArr)
    
