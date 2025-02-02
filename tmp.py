
def left(gear):
    gear.append(gear.popleft())

def right(gear):
    gear.appendleft(gear.pop())

from collections import deque
gears = [deque() for _ in range(4)]

for i in range(4):
    info = input()
    for j in range(len(info)):
        gears[i].append(info[j])


M = int(input())
for _ in range(M):
    cmd = list(map(int,input().split()))
    do_move = list()
    for i in range(3):
        if gears[i][2] == gears[i+1][-2]:
            do_move.append(0)
        else:
            do_move.append(1)
    #print(do_move)
    if cmd[0] == 1: ## 1-> 2-> 3-> 4
        if cmd[1] == -1:
            left(gears[0])
        else:
            right(gears[0])

        if do_move[0] == 1:
            if cmd[1] == -1:
                right(gears[1])
                if do_move[1] == 1:
                    left(gears[2])
                    if do_move[2] == 1:
                        right(gears[3])
            if cmd[1] == 1:
                left(gears[1])
                if do_move[1] == 1:
                    right(gears[2])
                    if do_move[2] == 1:
                        left(gears[3])

    elif cmd[0] == 2: ## 1<- 2-> 3-> 4
        if cmd[1] == -1:
            left(gears[1])
        else:
            right(gears[1])
        if do_move[0] == 1:
            if cmd[1] == -1:
                right(gears[0])
            elif cmd[1] == 1:
                left(gears[0])

        if do_move[1] == 1:
            if cmd[1] == -1:
                right(gears[2])
            elif cmd[1] == 1:
                left(gears[2])
                if do_move[2] == 1:
                    if cmd[1] == -1:
                        right(gears[3])
                    elif cmd[1] == 1:
                        left(gears[3])

    elif cmd[0] == 3: ## 1<- 2<- 3-> 4
        if cmd[1] == -1:
            left(gears[2])
        else:
            right(gears[2])

        if do_move[2] == 1:
            if cmd[1] == -1:
                right(gears[3])
            if cmd[1] == 1:
                left(gears[3])
        
        if do_move[1] == 1:
            if cmd[1] == -1:
                right(gears[1])
            elif cmd[1] == 1:
                left(gears[1])
                if do_move[0] == 1:
                    if cmd[1] == -1:
                        left(gears[0])
                    elif cmd[1] == 1:
                        right(gears[0])
        
                
    elif cmd [0] == 4: ## 1<- 2<- 3<- 4
        if cmd[1] == -1:
            left(gears[3])
        else:
            right(gears[3])

        if do_move[2] == 1:
            if cmd[1] == -1:
                right(gears[2])
                if do_move[1] == 1:
                    left(gears[1])
                    if do_move[0] == 1:
                        right(gears[0])
            if cmd[1] == 1:
                left(gears[2])
                if do_move[1] == 1:
                    right(gears[1])
                    if do_move[0] == 1:
                        left(gears[0])
    #my_gears(gears)
answer = 0
cnt = 1
for i in range(4):
    answer += int(gears[i][0])*cnt
    cnt *= 2

print(answer)
