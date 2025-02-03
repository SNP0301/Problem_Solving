"""
[복잡도] O(N**2)
    - 1000*1000의 바구니에 대해 완전탐색, 탐색 이후 0의 유무 검사를 위해 
    - 시간 초과

[구상]
    - 바구니 칸이 1이고 not visited면 bfs 실행 -> bfs 실행하면서 만난 갱신한 칸 수를 return -> 0이 아니면 answer.array에 저장
        - 갱신한 칸 수 +1 하고 queue.append(nx,ny,갱신한 칸 수)
        - return한 갱신 칸 수들 중 최대값이 정답
    - bfs 끝났는데도 0이 있으면 answer = -1
    - arr에 0은 없는데 bfs 결과값의 총합이 0이라면 (answer = 0이라면) 토마토가 익힌 토마토가 하나도 없다는 것이므로 정답은 0


[] 문제 읽기 -> [] I/O 확인 -> [] 제약조건/특이사항 확인 -> [] 구상 -> [] 복잡도 계산 -> [] 손 구현 -> [] 구현 -> [] 오픈테케 -> []히든테케
"""
import sys
input = sys.stdin.readline

def bfs(x,y,cur):
    queue = deque()
    queue.append((x,y,cur))
    visited[x][y] = True
    
    while queue:
        x,y,cur = queue.popleft()
        arr[x][y] = cur

        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]
            if 0<=nx<N+2 and 0<=ny<M+2 and arr[nx][ny] != -1:
                if not visited[nx][ny] and arr[nx][ny] != 1: ## 1) 들리지 않은 곳이고, 그 자리가 토마토 자리가 아닌 경우
                    queue.append((nx,ny,cur+1))
                    visited[nx][ny] = True
                elif arr[nx][ny] > cur+1: ## 2) 들렸던 곳인데 다른 토마토에 의해 익은 속도가 지금 잡은 토마토의 익힘 속도보다 느린 경우
                    queue.append((nx,ny,cur+1))
                    arr[nx][ny] = cur+1

    return cur


from collections import deque
M, N = map(int,input().split())


arr = [[-1 for _ in range(M+2)]] + [[-1] + list(map(int,input().split()))+[-1] for _ in range(N)] + [[-1 for _ in range(M+2)]]
for x in arr:
    print(x)

print()
visited = [[False for _ in range(M+2)] for _ in range(N+2)]
answer = 0
is_possible = True
mx = -1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(1,N+1):
    for y in range(1,M+1):
        if arr[x][y] == 1 and not visited[x][y]:
            answer += bfs(x,y,0)
            arr[x][y] = 1
        elif arr[x][y] == 0:
            zero_cnt = 0
            for f in range(4):
                nx = x+dx[f]
                ny = y+dy[f]
                if 0<=nx<N+2 and 0<=ny<M+2 and arr[nx][ny] == -1:
                    zero_cnt += 1
            if zero_cnt == 4:
                print("%d %d is zero_cnt 4"%(x,y))
                is_possible = False
                break


for x in arr:
    print(x)

if not is_possible:         ## 만약 모두 익히지 못했다면
    print(-1) 
elif is_possible:           ## 모두 익어있는데
    if answer == 0:         ## 원래 다 익었던거라면
        print(0)
    else:                   ## 하나라도 익혔다면
        print(mx)