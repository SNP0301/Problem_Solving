"""
* 시험에 도움이 되는 방향으로
** 같은 실수를 반복하지 말자
*** 지금 급하면 본 시험 때도 급하다
**** 시간 관리

[I/O]
    I: 격자의 상태
    O: 격자를 지울 수 있는 색종이 수의 최소값
"""
arr = [list(map(int,input().split())) for _ in range(10)]
pv = [5 for _ in range(5)]
answer = 5*5+1

def btk(cur_ans):
    global answer
    for x in range(10):
        for y in range(10):
            if arr[x][y] == 1:
                for sz in range(5):
                    nx = x + sz
                    ny = y + sz
                    if 0<=nx<10 and 0<=ny<10: ##범위 내
                        if pv[sz] >= 1:
                            possible = True
                            for ix in range(x,nx+1):
                                for iy in range(y,ny+1):
                                    if arr[ix][iy] != 1:
                                        possible = False
                                        break
                                if not possible: break
                            if possible:
                                for ix in range(x,nx+1):
                                    for iy in range(y,ny+1):
                                        arr[ix][iy] = 0
                                pv[sz] -= 1 #한장 쓸게
                                btk(cur_ans+1)
                                pv[sz] += 1 ## 원복
                                for ix in range(x,nx+1):
                                    for iy in range(y,ny+1):
                                        arr[ix][iy] = 1



    answer = min(cur_ans,answer)




if answer == 5*5+1: print(-1)
else: print(answer)