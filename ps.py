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


def bfs(x,y):
    global k
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 0
    answer = 0
    while q:
        if cnt >= k:
            break
        x,y = q.popleft()
        for i in range(4):
            nextX = x+dx[i]
            nextY = y+dy[i]

            if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:
                continue

            if visited[nextX][nextY] == 0:
                visited[nextX][nextY] = 1
                q.append((nextX, nextY))
                answer += graph[nextX][nextY]
                cnt += 1
                for p in range(4):
                    if nextX+dx[p] < 0 or nextY+dy[p] < 0 or nextX+dx[p] >= n or nextY+dy[p] >= m:
                        continue
                    if visited[nextX+dx[p]][nextY+dy[p]] != 1:
                        q.append((nextX+dx[p],nextY+dy[p]))
                        visited[nextX+dx[p]][nextY+dy[p]] = "N"
            elif visited[nextX][nextY] == "N":
                for p in range(4):
                    if nextX+dx[p] < 0 or nextY+dy[p] < 0 or nextX+dx[p] >= n or nextY+dy[p] >= m:
                        continue
                    if visited[nextX+dx[p]][nextY+dy[p]] == 0:
                        q.append((nextX+dx[p],nextY+dy[p]))
            if cnt >= k:
                    break
    print(answer)   
    check(visited)

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

