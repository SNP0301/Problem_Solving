'''
[BOJ] 13023. ABCDE
T: 2초
M: 512MB
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
is_it_possible = False

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

##print(graph)

def dfs(x,length):
    global is_it_possible
    if length == 5:
        is_it_possible = True
        return
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i,length+1)
    visited[x] = 0

    
for i in range(n):
    dfs(i,1)
    if is_it_possible:
        break

if is_it_possible:
    print(1)
else:
    print(0)