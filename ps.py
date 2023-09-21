'''
[BOJ] 1707. 이분 그래프
T: 2s
M: 128MB
'''
import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
graph = list()

def bfs(x,color_int):
    q = deque()
    q.append((x,color_int))
    while q:
        nextX,next_color_int = q.popleft()
        for i in range(v):
            if graph[nextX][i] == 0:
                continue
            elif graph[nextX][i] == 1:
                graph[nextX][i] *= next_color_int
                graph[i][nextX] *= next_color_int
                q.append((nextX,next_color_int*-1))
            elif graph[nextX][i] + next_color_int != 0:
                print("ERRORRORORORORO")
            

 
def check_array(array):
    for a in array:
        print(a)
    print("\n")

for _ in range(k):################################################################ k
    v,e = map(int,input().split())
    graph = [[0 for _ in range(v)] for _ in range(v)]
    
    for _ in range(e):
        u,v = map(int,input().split())
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1
    #check_array(graph)

    
    for i in range(v):
        for j in range(v):
            if graph[i][j] == 1:
                bfs(i,3)
    
    check_array(graph)


    