"""

"""
def dfs(c):
    visited[c] = True
    ans_dfs.append(c)
    for i in adj[c]:
        if not visited[i]: dfs(i)

def bfs(s):
    queue = []
    visited[s] = True
    queue.append(s)
    ans_bfs.append(s)
    while queue:
        c = queue.pop(0)
        for i in adj[c]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                ans_bfs.append(i)
        ##visited[c] = True


N,M,V = map(int,input().split())
visited = [False for _ in range(N+1)]
ans_dfs = []
ans_bfs = []

adj = [[] for _ in range(N+1)]

for _ in range(M):
    start,end = map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)

for i in adj:
    i.sort()

dfs(V)
visited = [False for _ in range(N+1)]
bfs(V)
print(*ans_dfs)
print(*ans_bfs)



