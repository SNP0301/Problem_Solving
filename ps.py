'''
[BOJ] 13023. ABCDE
T: 2s
M: 512MB
'''
import sys
input = sys.stdin.readline
from collections import deque


n, k = map(int,input().split())
lastIndex = 100000

graph = [0 for i in range(lastIndex+1)]
from_graph = [0 for i in range(lastIndex+1)]

def bfs(x):
    q = deque()
    cnt = 1
    q.append(x)
    graph[x] = 1


    while q:
        x = q.popleft()
        dx = [x-1, x+1, x*2]
        ##print("[%d]: (%d, %d, %d)"%(x,dx[0],dx[1],dx[2]))
        for i in range(3):
            nextX = dx[i]

            if nextX < 0 or nextX >= lastIndex+1:
                continue
                
            if graph[nextX]==0:
                q.append(nextX)
                graph[nextX] = graph[x]+1
                from_graph[nextX] = x

        if(graph[k]!=0):
            print(graph[k]-1)
            break
        else:
            cnt += 1


bfs(n)
z = k
answer = [k]
while z != n:
    answer.append(from_graph[z])
    z = from_graph[z]

for i in range(len(answer)-1,-1,-1):
    print(answer[i],end=" ")





