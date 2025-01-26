"""
* 회전이나 대칭을 시켜도 된다.

[구상]
- 5개의 테트로미노가 각각 탐색하는 위치를  dx,dy로 저장
    - 예시 1) 하늘색 테트로미노: dx = [0,0,0], dy = [1,2,3]
    - 예시 2) 노란색 테트로미노: dx = [0,1,1], dy = [1,0,1]
- 각 테트로미노의 dx,dy는 바꾸지 않고 (테트로미노는 회전시키지 않고) 종이를 zip으로 돌린다
    - 첫 상태를 포함해 총 4장의 종이에 대해 탐색
    - 대칭까지 가능하므로 *2번 탐색
- N*M*4*5*2이므로 탐색은 최대 500*500*4*5*2 = 10000000

[확인할 것]
- 10000000번이 맞는지, 이 숫자를 괜찮다고 봐도 괜찮은지 (2초, 512MB)
"""

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
answer = -1

blue_dx = [0,0,0]
blue_dy = [1,2,3]

yellow_dx = [0,1,1]
yellow_dy = [1,0,1]

orange_dx = [1,2,2]
orange_dy = [0,0,1]

green_dx = [1,1,2]
green_dy = [0,1,1]

pink_dx = [0,0,1]
pink_dy = [1,2,1]

dx = [blue_dx, yellow_dx, orange_dx, green_dx, pink_dx]
dy = [blue_dy, yellow_dy, orange_dy, green_dy, pink_dy]

x_s = [1,-1,1,-1]
y_s = [1,1,-1,-1]


for r in range(4): # r of rotate
    for x in range(N):
        for y in range(M):
            current_answer = arr[x][y]
            for t in range(5): # t of type
                current_answer = arr[x][y]
                for s in range(3): # s of  symmetry
                    current_answer = arr[x][y]
                    for d in range(3): # d of depth
                        ndx = x+(dx[t][d]*x_s[s])
                        ndy = y+(dy[t][d]*y_s[s])
                        if 0<=ndx<N and 0<=ndy<M:
                            current_answer += arr[ndx][ndy]
                            ##print("[%d,%d]:%d"%(ndx,ndy,arr[ndx][ndy])
                            if d == 2:
                                ##print("%d makes %d from t:[%d], from [%d,%d] to [%d,%d]"%(arr[ndx][ndy],current_answer,t,x,y,ndx,ndy))
                                answer = max(answer,current_answer)
                                current_answer = arr[x][y]
                        else:
                            break   

    arr = [[row[col] for row in arr] for col in range(len(arr[0]))]
    N, M = M, N
print(answer)