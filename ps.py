'''
[BOJ] 7576. 토마토
T: 1 second
M: 256 MB
'''

from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
graph = list()
q = deque()
answer = 1
possible = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q.append((x,y))
    
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nextX = x + dx[i]
                nextY = y + dy[i]

                if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:
                    continue
                if graph[nextX][nextY] == 0:
                    q.append((nextX,nextY))
                    graph[nextX][nextY] = graph[x][y] + 1


for _ in range(n):
    graph.append(list(map(int,input().split())))

for a in range(n):
    for b in range(m):
        if graph[a][b] == 1:
            q.append((a,b))

bfs(q[0][0],q[0][1])

for k in graph:
    answer = max(answer,max(k))
    if 0 in k:
        possible =  False

if possible:
    print(answer-1)
else:
    print(-1)
