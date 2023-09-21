'''
[BOJ] 1707. 이분 그래프
T: 2s
M: 128MB
'''
import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
graph = list()

def bfs(x, color):
    q = deque([x])
    visited[x] = color
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[x]*-1
            elif visited[i] + visited[x] != 0:
                return False
    return True

for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v)]
    visited = [0 for _ in range(v)]

    ##print("visited:",visited)
    
    for _ in range(e):
        u,v = map(int,input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    

    for i in range(v):
        if not visited[i]:
            result = bfs(i,3)
            if not result:
                break
    if result: print('YES')
    else: print('NO')
