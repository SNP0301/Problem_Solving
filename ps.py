'''
[BOJ] 7569. 토마토
T: 1 second
M: 256 MB

3차원 힌트
print(graph[0][0][0]) ## 1  (시작)
print(graph[0][0][1]) ## 2  (행)
print(graph[0][1][0]) ## 4  (열)
print(graph[1][0][0]) ## 10 (층)
'''

import sys
from collections import deque
input = sys.stdin.readline

twoDimensionalGraph = list()
graph = list()
q = deque()
possible = True
answer = 1

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

m,n,h = map(int,input().split())


for _ in range(h):
    for _ in range(n):
        twoDimensionalGraph.append(list(map(int,input().split())))
    graph.append(twoDimensionalGraph)
    twoDimensionalGraph = []



def bfs(x,y,z):
    q.append((x,y,z))

    while q:
        for _ in range(len(q)):
            x,y,z, = q.popleft()
            for i in range(6):
                nextX = x + dx[i]
                nextY = y + dy[i]
                nextZ = z + dz[i]

                if nextX < 0 or nextY < 0 or nextZ < 0 or nextX >= n or nextY >= m or nextZ >= h:
                    continue
                if graph[nextZ][nextX][nextY] == 0:
                    q.append((nextX, nextY, nextZ))
                    graph[nextZ][nextX][nextY] = graph[z][x][y] + 1


for c in range(h):
    for a in range(n):
        for b in range(m):
            ##print("(a: %d, b: %d, c:%d)"%(a,b,c))
            if graph[c][a][b] == 1:
                q.append((a,b,c))



if q:
    bfs(q[0][0],q[0][1],q[0][2])
else:
    possible = False


for u in graph:
        for v in u:
            answer = max(answer,max(v))
            if 0 in v:
                possible = False

if possible:
    print(answer-1)
else:
    print(-1)
