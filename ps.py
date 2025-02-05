"""
[복잡도] O(N+M)
    - N개의 노드와 M개의 간선에 대해 완전탐색
[구상]
    I: 노드와 간선의 수, 단방향 간선의 연결 정보
    O: (오름차순) 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호

[보완할 점]
    - (89590503) N이 10,000이고 M이 100,000이어서 시간초과/메모리초과를 과도하게 고려
                                                ㄴ 감각,,,
"""
from collections import deque
def bfs(s):
    cnt = 0
    visited = [False]*(N+1)        ## 컴퓨터 수가 1부터 시작하므로 N+1로 선언
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        s = queue.popleft()
        for i in adj[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt                      ## 해킹할 수 있는 컴퓨터 수 반환

N, M = map(int,input().split())
adj = [[] for _ in range(N+1)]      ## 컴퓨터 수가 1부터 시작하므로 N+1로 선언
mx = -1
mx_lst = list()

for _ in range(M):
    e,s = map(int,input().split()) 
    adj[s].append(e)                ##  단방향

for i in range(1,N+1):
    h = bfs(i)
    if h > mx:                      # 최대값 갱신
        mx = h
        mx_lst = list()
        mx_lst.append(i)
    elif h == mx:                   # 현재의 최대값과 같은 값을 갖는 컴퓨터 추가
        mx_lst.append(i)


mx_lst.sort()

for i in mx_lst:
    print(i,end=" ")