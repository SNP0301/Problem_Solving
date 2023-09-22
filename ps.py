'''
[BOJ] 18290. NM과 K(1)
T: 2s
M: 512MB
'''
import sys
input = sys.stdin.readline
from collections import deque

def check(g):
    for i in g:
        print(i)     

n,m,k = map(int,input().split())
##visited = [[0 for _ in range(m)] for _ in range(n)]

graph = list()
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer_list = list()
#check(visited)
#check(graph)

def bfs(x,y):
    global k
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 0
    answer = 0
    while q:
        if cnt >= k:
            break
        x,y = q.popleft()
        for i in range(4):
            nextX = x+dx[i]
            nextY = y+dy[i]

            if nextX < 0 or nextY < 0 or nextX >= m or nextY >= n:
                continue
            if visited[nextX][nextY] == 0:
                q.append((nextX, nextY))
                answer += graph[nextX][nextY]
                cnt += 1
    return answer

for i in range(m):
    for j in range(n):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        answer_list.append(bfs(i,j))

print(max(answer_list))
