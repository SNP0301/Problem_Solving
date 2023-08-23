'''
[BOJ] 2606. 바이러스
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

C = int(input()) ### # of computers
P = int(input()) ### # of pair of computer connections

graph = [[]for _ in range(C+1)]
visitedDfs = [0 for _ in range(C+1)]
answer = 0

for _ in range(P):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in graph:
    i.sort()

def dfs(n):
    global answer
    visitedDfs[n] = 1

    for i in graph[n]:
        if not visitedDfs[i]:
            dfs(i)
            answer += 1


dfs(1)

print(answer)