'''
[BOJ] 16928. 뱀과 사다리 게임
T: 1초
M: 512MB
'''

import sys
input = sys.stdin.readline
from collections import deque

MAX_INDEX = 20 + 1

n,m = map(int,input().split())

item_graph = [0 for _ in range(MAX_INDEX)]
board_graph = [0 for i in range(MAX_INDEX)]
board_graph[1] = 1
board_graph[MAX_INDEX-1] =999

dx = [1,2,3,4,5,6]

def check_graph():
    print(board_graph)
    print(item_graph)

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for i in range(6):
            nextX = x + dx[i]
            
            if nextX >= MAX_INDEX:
                continue
            if board_graph[nextX] == 0:
                q.append(nextX)
                board_graph[nextX] = board_graph[x] + 1

            

for _ in range(n+m):
    u,v = map(int,input().split())
    item_graph[u] = v

bfs(1)

check_graph()

print(board_graph[MAX_INDEX-1])