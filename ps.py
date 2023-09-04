import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())
answer = 0
cb_answer = 0

graph = list()
visited = [[False]*n for _ in range(n)]

cb_graph = list()
cb_visited = [[False]*n for _ in range(n)]

for _ in range(n):
    line = input().rstrip()
    graph.append(line)
    line = line.replace('G','R')
    cb_graph.append(line)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = True

    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0:
            continue
        if visited[nextX][nextY] == False and graph[x][y] == graph[nextX][nextY]:
            dfs(nextX, nextY)

def cb_dfs(x,y):
    cb_visited[x][y] = True

    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0:
            continue
        if cb_visited[nextX][nextY] == False and cb_graph[x][y] == cb_graph[nextX][nextY]:
            cb_dfs(nextX, nextY)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            answer += 1
        if cb_visited[i][j] == False:
            cb_dfs(i,j)
            cb_answer += 1

print(answer)
print(cb_answer)
            

