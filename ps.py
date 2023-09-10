'''
[BOJ] 2206. 벽 부수고 이동하기
T: 1초
M: 512MB
'''

import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = list()
q = deque
q.append((0,0))
breakable = True

for i in range(n):
    graph.append(list(map(int,input().strip())))



dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    x,y = q.popleft()
    
    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        
        if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:
            continue
        if graph[nextX][nextY] == 0:
            



def check_graph():
    for i in graph:
        print(i)

check_graph()