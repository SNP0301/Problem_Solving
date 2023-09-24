'''
[BOJ] 14226. 이모티콘
T: 2s
M: 512MB
'''
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
MAX_INDEX = n*2+1

graph = [i for i in range(MAX_INDEX)]
graph[1] = 0

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        i = 1
        while x*i < MAX_INDEX:
            if i == 2:
                graph[x*i] = min(graph[x*i],graph[x]+2)
                i += 1
            else:
                if graph[x*i] > graph[x]+1:
                    graph[x*i] = graph[x]+i
                    q.append(x*i)
                if graph[x*i-1] > graph[x*i]+1:
                    graph[x*i-1] = graph[x*i]+1
                i += 1

bfs(1)
print(graph)
print(graph[n])