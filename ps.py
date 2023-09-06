import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = list()

for i in range(n):
    line = list(input().rstrip())
    graph.append([int(x) for x in line])

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nextX = x+ dx[i]
            nextY = y+ dy[i]

            if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:
                continue
            if graph[nextX][nextY] == 1:
                graph[nextX][nextY] = graph[x][y] + 1
                q.append((nextX, nextY))

    return graph[n-1][m-1]

print(bfs(0,0))



