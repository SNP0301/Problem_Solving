'''
[BOJ] 1260. DFS와 BFS
'''


from collections import deque

N,M,V = map(int, input().split())

graph = [[False]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

visitedDfs = [False]*(N+1)
visitedBfs = [False]*(N+1)

def dfs(V): 
    visitedDfs[V] = True
    print(V,end=" ")
    for i in range(1,N+1):
        if not visitedDfs[i] and graph[V][i]:
            dfs(i)


def bfs(V):
    q = deque([V])
    visitedBfs[V] = True
    while q:
        V = q.popleft()
        print(V,end=" ")
        for i in range(1, N+1):
            if not visitedBfs[i] and graph[V][i]:
                q.append(i)
                visitedBfs[i] = True


dfs(V)
print()
bfs(V)