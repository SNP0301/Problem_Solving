'''
[BOJ] 6603. 로또
T: 1s
M: 128MB
'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def show(K:int, S:list, is_visited:list):
    for i in range(0,K):
        if is_visited[i]:
            print(S[i], end=' ')
    print()

def dfs(l,arr,visited,i,cnt):
    if cnt == 6:
        show(l,arr,visited)
        return
    for x in range(i,l):
        if visited[x]:
            continue
        visited[x] = True
        dfs(l,arr,visited,x,cnt+1)
        visited[x] = False

while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    else:
        l = arr[0]
        visited = [False for _ in range(l)]
        dfs(l,arr[1:],visited,0,0)
        print()