"""
[시간복잡도] O(N**2)
    - 전체 사람에 대해 완전탐색하므로, 100*100

    
* 베이컨 수 최소값이 같은 사람이 둘 이상인 경우 번호가 가장 작은 사람 출력 -> 작은 사람부터 bfs 시작, 더 작을 때만 갱신(같을 때는 갱신 x)
** 친구 관계가 중복으로 들어올 수도 있다 -> 집합으로 adj 관리
"""
from collections import deque

def bfs(s):
    visited = [1] + [0 for _ in range(N)]
    arr = [0] + [0 for _ in range(N)]
    queue = deque()
    queue.append((s,0))
    visited[s] = 1
    while queue:
        s, score = queue.popleft()
        for x in adj[s]:
            if not visited[x]:
                arr[x] += score + 1
                visited[x] = True
                queue.append((x,score+1))

    return sum(arr)




N, M = map(int,input().split())
adj = [set() for _ in range(N+1)]
cur_min = N*M+1
answer = 1
for _ in range(M):
    s,e = map(int,input().split())
    adj[s].add(e)
    adj[e].add(s)


for i in range(1,N+1):
    b = bfs(i)
    if b < cur_min:
        answer = i
        cur_min = b

print(answer)