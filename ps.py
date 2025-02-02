from collections import deque

def check_move(gears):
    do_move = [0,0,0]
    for i in range(3):
        if gears[i][2] != gears[i+1][6]:
            do_move[i] = 1
    return do_move

def rotate(gear_num,watch): ## rotate(돌릴 기어의 번호, 시계 Or 반시계, from 왼쪽 방향 -1 or 오른쪽 방향 +1)
    if watch == 1: ## 시계방향으로 돌리면
        rotate_right(gear_num)
    elif watch == -1: ## 반시계방향으로 돌리면
        rotate_left(gear_num)
    elif watch == 0:
        pass

def rotate_left(gear_num):                              #반시계 방향
    gears[gear_num].append(gears[gear_num].popleft())

def rotate_right(gear_num):                             ## 시계 방향
    gears[gear_num].appendleft(gears[gear_num].pop())

gears = list()
for _ in range(4):
    gears.append(deque(map(int,input())))

M = int(input())
for _ in range(M):
    start_gear, watch = map(int,input().split())
    do_move = check_move(gears)
    #my_print(gears)
    if start_gear == 1:
        rotate(0,watch)
        rotate(1,-1*watch*do_move[0])
        if do_move[1] == 1:
            rotate(2,watch*do_move[1])
            if do_move[2] == 1:
                rotate(3,-1*watch)
    elif start_gear == 2:
        rotate(0,-1*watch*do_move[0])
        rotate(1,watch)
        rotate(2,-1*watch*do_move[1])
        if do_move[1]*do_move[2] == 1:
            rotate(3,watch)
    elif start_gear == 3:
        rotate(1,-1*watch*do_move[1])
        rotate(2,watch) 
        rotate(3,-1*watch*do_move[2])
        if do_move[0]*do_move[1] == 1:
            rotate(0,watch)
    elif start_gear == 4:
        rotate(2,-1*watch*do_move[2])
        rotate(3,watch)
        if do_move[1] == 1:
            rotate(1,watch*do_move[1])
            if do_move[0] == 1:
                rotate(0,-1*watch*do_move[0])


    ##my_print(gears)

#my_print(gears)
answer = 0
cnt = 1
for g in gears:
    answer += g[0]*cnt
    cnt *= 2

print(answer)