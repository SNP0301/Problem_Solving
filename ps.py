'''
[BOJ] 24480. 알고리즘 수업 - 깊이 우선 탐색 2
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]
visitedDfs = [0 for _ in range(n+1)]
count = 0

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)


def dfs(num):
    global count
    count += 1
    visitedDfs[num] = count
    for i in graph[num]:
        if not visitedDfs[i]:
            dfs(i)

dfs(r)

for i in range(1,n+1):
    print(visitedDfs[i])
