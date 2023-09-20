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
    ##print(graph)

    while q:
        if visited[k]:
            print(graph[k])
            ##print(graph)
            break
        x = q.popleft()
        dx = [x*2,x-1,x+1]

        for i in range(3):
            nextX = dx[i]

            if nextX == 0 and not visited[nextX]:
                visited[nextX] = True
                graph[nextX] = graph[x]+1
            elif  nextX < 0 or nextX >= lastIndex+1:
                continue
            
            if i != 0 and (not visited[nextX] or (visited[nextX] and graph[nextX] > graph[x]+1)):
                graph[nextX] = graph[x] + 1
                visited[nextX] = True
                q.append(nextX)
            elif  i == 0 and (not visited[nextX] or (visited[nextX] and graph[nextX] > graph[x]+1)) :
                graph[nextX] = graph[x]
                visited[nextX] = True
                q.append(nextX)
            ##print(graph)

        if visited[k]:
            print(graph[k])
            ##print(graph)
            break

bfs(n)
