'''
[BOJ] 13549. 숨바꼭질 3
T: 2초
M: 512MB
'''
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
lastIndex = 20
graph = [0 for i in range(lastIndex+1)]
has_been_teleported = [0 for i in range(lastIndex+1)]

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        if(graph[k]!=0):
            print(graph[k])
            break
        cnt = 2
        x = q.popleft()
        dx = [x-1, x+1, x*2]
        
        for i in range(3):
            nextX = dx[i]
        
            if nextX < 0 or nextX >= lastIndex+1:
                continue
            if graph[nextX]==0 and i!=2:
                graph[nextX] = graph[x]+1
                q.append(nextX)
            elif i == 2:
                graph[nextX] = graph[x]
                q.append(nextX)
                has_been_teleported[nextX] = True

                while nextX*2**(cnt) < lastIndex+1 and has_been_teleported[nextX*2**(cnt)] == False:
                    has_been_teleported[nextX*2**(cnt)] = True
                    graph[nextX*2**(cnt)] = graph[x]
                    q.append(nextX*2**(cnt))






bfs(n)
print(graph)