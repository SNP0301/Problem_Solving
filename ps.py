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

n,m,k = map(int,input().split())


graph = list()
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer_list = list()


def bfs(x,y):
    global k
    q = deque()
    q.append((x,y))
    visited[x][y] = "P"
    cnt = 0
    answer = 0
    while q:

        x,y = q.popleft()
        for i in range(4):
            nextX = x+dx[i]
            nextY = y+dy[i]

            if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:
                continue
            q.append((nextX, nextY))
            if visited[nextX][nextY] == 0:
                visited[nextX][nextY] = "P"
                for k in range(4):
                    if nextX+dx[k] < 0 or nextY+dy[k] < 0 or nextX+dx[k] >= n or nextY+dy[k] >= m:
                        continue
                    visited[nextX+dx[k]][nextY+dy[k]] = "N"

                print(cnt,answer,graph[nextX][nextY])
                answer += graph[nextX][nextY]
                cnt += 1
            elif visited[nextX][nextY] == "N":
                for k in range(4):
                    if nextX+dx[k] < 0 or nextY+dy[k] < 0 or nextX+dx[k] >= n or nextY+dy[k] >= m:
                        continue
                    q.append((nextX+dx[k], nextY+dy[k]))
        if cnt >= k:
            break

    for x in visited:
        print(x)
    print(answer,"\n")
    return answer

if n==1 and m == 1:
    print(graph[0][0])
    exit()
else:
    for i in range(n):
        for j in range(m):
            visited = [[0 for _ in range(m)] for _ in range(n)]
            answer_list.append(bfs(i,j))

print(answer_list)
print(max(answer_list))

