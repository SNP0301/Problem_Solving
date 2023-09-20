'''
[BOJ] 13549. 숨바꼭질 3
T: 2초
M: 512MB
'''
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
lastIndex = 200000

graph = [0 for i in range(lastIndex+1)]
visited = [False for i in range(lastIndex+1)]

q = deque()

def bfs(x):
    q.append(x)
    graph[x] = 0
    visited[x] = True

    while q:
        if visited[k]:
            print(graph[k])
            break
        x = q.popleft()
        dx = [x-1,x+1,x*2]

        for i in range(3):
            nextX = dx[i]

            if nextX == 0:
                visited[nextX] = True
                graph[nextX] = graph[x]+1
            elif  nextX < 0 or nextX >= lastIndex+1:
                continue
            
            if not visited[nextX] and i != 2:
                graph[nextX] = graph[x] + 1
                visited[nextX] = True
                q.append(nextX)
            elif (not visited[nextX] or graph[nextX] >= graph[x])and i == 2:
                graph[nextX] = graph[x]
                visited[nextX] = True
                q.append(nextX)

bfs(n)
