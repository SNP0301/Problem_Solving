"""

"""
def dfs(c):
    visited[c] = True
    for i in adj[c]:
        if not visited[i]: dfs(i)

N, M = map(int,input().split())
visited = [False for _ in range(N+1)]
adj = [[] for _ in range(N+1)]
answer = 0

for _ in range(M):
    start, end = map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        answer += 1
print(answer)




