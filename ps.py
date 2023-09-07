import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
graph = list()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 1
    global cnt
    answer = 0
    while q:
        x,y = q.popleft() 
        
        cnt += 1

        for i in range(4):

            nextX = x + dx[i]
            nextY = y + dy[i]
            if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:
                continue
            if graph[nextX][nextY] == 0:
                q.append((nextX,nextY))
                graph[nextX][nextY] = graph[x][y] + 1

    print(graph)


for a in range(n):
    for b in range(m):
        if graph[a][b] == 1:
            bfs(a,b)
print(cnt)

               
