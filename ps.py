import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
graph = [0]* 1000001
cnt = 1


def bfs(x):
    global cnt
    q = deque()
    q.append((x))
    while q:
        x = q.popleft()
        nextX = [x-1, x+1, 2*x]
        for i in range(3):
            if nextX[i] < 0 or nextX[i] >= 100000:
                continue
            if graph[nextX[i]-1] == 0:
                q.append((nextX[i]-1))
                graph[nextX[i]-1] = cnt
        if  graph[k] != 0:
            return(graph[k]-1)
        cnt += 1

print(int(bfs(n)+1))