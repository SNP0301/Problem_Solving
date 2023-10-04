'''
[BOJ] 18290. NM과 K(1)
T: 2s
M: 512MB
'''
import sys
input = sys.stdin.readline
from collections import deque

def check(g):
    for i in g:
        print(i)   
    print("\n")  

n,m,k = map(int,input().split())


graph = list()
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer_list = list()


def bfs(x,y,visited):

    q = deque()
    q.append((x,y))
    answer = 0
    cnt = 1
    visited[x][y] = "P"

    while q:
        if cnt >= k:
            answer_list.append(answer)
            return
        x,y = q.popleft()
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]

            if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:
                continue
            if visited[nextX][nextY] == 0:
                answer += graph[nextX][nextY]
                visited[nextX][nextY] = "P"
                cnt += 1
                for b in range(4):
                    blockX = nextX + dx[b]
                    blockY = nextY + dy[b]
                    if blockX < 0 or blockY < 0 or blockX >= n or blockY >= m:
                        continue
                    visited[blockX][blockY] = 1
                    q.append((blockX,blockY))
            else: #if visited[nextX][nextY] != 0:
                for b in range(4):
                    blockX = nextX + dx[b]
                    blockY = nextY + dy[b]
                    if blockX < 0 or blockY < 0 or blockX >= n or blockY >= m:
                        continue
                    visited[blockX][blockY] = 1
                    q.append((blockX,blockY))

        if cnt >= k:
            print(answer)
            check(visited)
            answer_list.append(answer)
            return

if m + n == 2:
    print(graph[0][0])
elif m+n != 2 and k == 1:
    for i in range(n):
        answer_max = max(max(graph[i]),-100)
    print(answer_max)
else:
    for i in range(n):
        for j in range(m):
            visited = [[0 for _ in range(m)] for _ in range(n)]
            bfs(i,j,visited)
    print(answer_list)
    print(max(answer_list))