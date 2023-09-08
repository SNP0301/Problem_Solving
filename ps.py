import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

def bfs(x,y):
    cnt = 0
    q = deque()
    q.append((x,y))
    graph[x][y] = 1

    while q: 
        x,y = q.popleft()
        
        
        for j in range(8):
            nextX = x + dx[j]
            nextY = y + dy[j]

            if nextX < 0 or nextY < 0 or nextX >= i or nextY >= i:
                continue
            if graph[nextX][nextY] == 0:
                q.append((nextX,nextY))
                graph[nextX][nextY] = graph[x][y] + 1
        
        if(graph[endX][endY] != 0):
            print(graph[endX][endY]-1)
            break


for _ in range(t):
    i = int(input())
    graph = [[0]*i for _ in range(i)]
    visited = [[False]*i for _ in range(i)]
    startX, startY = map(int,input().split())
    endX, endY = map(int,input().split())

    bfs(startX,startY)
