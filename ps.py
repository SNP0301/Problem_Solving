from collections import deque
import sys
input = sys.stdin.readline


t = int(input())

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]


def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        graph[x][y] = cnt

        for k in range(8):
            nextX = x + dx[k]
            nextY = y + dy[k]

            if nextX < 0 or nextY < 0 or nextX >= i or nextY >= i:
                continue
            if x == endX and y == endY:
                print(graph[endX][endY])
                return
            if graph[nextX][nextY] == 0:
                q.append((nextX,nextY))
                graph[nextX][nextY] = cnt
                cnt += 1

for _ in range(t):
    i = int(input())
    cnt = 1
    graph = [[0]*i for _ in range(i)]
    startX, startY = map(int,input().split())
    endX, endY = map(int,input().split())

    if(startX == endX and startY == endY):
        print(0)
    else:
        bfs(startX, startY)
    