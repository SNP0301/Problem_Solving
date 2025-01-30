"""
단위 작업 내용 및 순서를 아직 잘 모르는 것 같다.
반복문, 조건문 등이 각각 언제/무엇을/언제까지 하는 것인지 명확하게 이해하고 구현할 것.


* K*2로 두거나, 반복문으로 앞으로 갔다가 뒤로 갔다면 못 풀었던 이유 찾아내기
"""

from collections import deque
def bfs(s): # 방문 표시?
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        cur = q.popleft()
        #print(cur, q)
        for next in [cur-1,cur+1,cur*2]:
            if next == K:
                return arr[cur] + 1 ##
            elif 0<=next<=100000 and not visited[next]:
                arr[next] = arr[cur] + 1
                q.append(next)
                visited[next] = True



N, K = map(int,input().split())
arr = [0 for _ in range(100001)] # 0부터니까 갯수만큼 선언해도 ㄱㅊ
visited = [ False for _ in range(100001)]
if K == N:
    print(0)
else:
    print(bfs(N))