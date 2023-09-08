'''
[BOJ] 7569. 토마토
T: 1 second
M: 256 MB
'''

from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = list()
q = deque()
answer = 1
possible = True

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(x,y,z):
    q.append((x,y,z))
    
    while q:
        for _ in range(len(q)):
            x,y,z = q.popleft()
            for i in range(6):
                nextX = x + dx[i]
                nextY = y + dy[i]
                nextZ = z + dx[i]

                if nextX < 0 or nextY < 0 or nextZ < 0 or nextX >= n or nextY >= m or nextZ >= h:
                    continue
                if graph[nextX][nextY][nextZ] == 0:
                    q.append((nextX,nextY,nextZ))
                    graph[nextX][nextY][nextZ] = graph[x][y][z] + 1


for _ in range(h):
    line = list()
    for _ in range(n):
        line.append(list(map(int,input().split())))
    graph.append(line)

for c in range(h):
    for a in range(n):
        for b in range(m):
            if graph[c][a][b] == 1:
                q.append((c,a,b))

if q:
    bfs(q[0][0][0],q[0][0][1])
else:
    possible = False

for k in graph:
    answer = max(answer,max(k))
    if 0 in k:
        possible = False

if possible:
    print(answer-1)
else:
    print(-1)
