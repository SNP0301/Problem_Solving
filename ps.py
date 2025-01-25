"""
* 구사과의 돌의 개수와 큐브러버의 돌의 개수는 항상 일치
** 아직 승자가 정해지지 않은 상태로 입력
*** 바둑판 크기는 10*10으로 고정

[배운 것]
- 

[구상]
- 'X'를 10*10에 각각 놓는 시행
    - 단, 놓으려는 자리에 '.'이 아닌 다른 값이 있으면 continue
- 'X'를 놓은 자리에서 8방향으로 탐색
    - arr[x][y]: 'X'를 놓으려는 자리
    - arr[nx][ny]: 탐색하려는 자리
        - 조건 1) 탐색하려는 자리는 arr를 벗어나지 않아야 한다
        - 조건 2) arr[nx][ny] == 'X'

[얘기해보면 좋을 것]
- 8방향 탐색할 때 방향 배열 어떻게 입력하시는지
"""
arr = list()
dx = [-1,0,1, 1,1,0, -1,-1]
dy = [1,1,1, 0,-1,-1, -1,0]
is_winnable = False

for _ in range(10):
    arr.append(list(input()))

################################################################
for x in range(10):
    for y in range(10):
        if arr[x][y] != 'O':
            for e in range(8): ## e of eight, 탐색 방향 바뀔 때마다 cnt와 turn 부여
                cnt = 1 ## arr[x][y]가 "O"였다면 반복문에 들어오지 못하고, "X"면 들어오고, "."이면 턴을 한번 사용하고 들어온다
                turn_used = False 

                if arr[x][y] == '.': 
                    if not turn_used:
                        turn_used = True

                for f in range(1,5): ## f of four
                    nx = x + dx[e]*f
                    ny = y + dy[e]*f
                    if 0<=nx<10 and 0<=ny<10: #arr 밖으로 벗어나지 않는지 확인
                        if arr[nx][ny] == 'X':
                            cnt += 1
                        elif arr[nx][ny] == '.':
                            if not turn_used:
                                cnt += 1
                                turn_used = True ## 턴을 한번 사용하고 탐색한 자리에 "X"를 뒀다고 가정, 갯수를 추가
                            else:
                                break
                        else:
                            break
                        if cnt == 5:
                            is_winnable = True
                            ##print("can win from (%d, %d) to (%d,%d)"%(x,y,nx,ny))
                            break
                    else:
                        break
if is_winnable:
    print(1)
else:
    print(0)
################################################################