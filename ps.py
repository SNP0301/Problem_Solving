'''
[BOJ] 24479. 알고리즘 수업 - 깊이 우선 탐색 1
'''

import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())

graph = [[False]*(n+1) for _ in range(n+1)]
visitedDfs = [False]*(n+1)


for _ in range(m):
    u,v = map(int,input().split())
    graph[u][v] = True
    graph[v][u] = True

def dfs(R):
    visitedDfs[R] = True
    print(R)
    for i in range(1, n+1):
        if not visitedDfs[i] and graph[R][i]:
            dfs(i)


dfs(r)
for i in range(1,len(visitedDfs)):
    if not visitedDfs[i]:
        print(0)