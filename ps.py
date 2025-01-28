"""

"""

def get_cur_N(cable_size,K):
    cur_N = 0
    for i in range(K):
        cur_N += cables[i]//cable_size
    return int(cur_N)

K, N = map(int,input().split())
cables = list()

for _ in range(K):
    cables.append(int(input()))
cable_size = 1
move_size = 1
going_up = True
going_down = not going_up
answer = list()
while True:
    if N == 1:
        print(cables[0])
        break
    else:
        cur_N = get_cur_N(cable_size,K)

        if going_up:
            if cur_N >= N: ## P1. 등호 위치
                move_size *= 2
                cable_size += move_size
            elif cur_N < N:
                move_size /= 2
                cable_size -= move_size
                going_down = True
                going_up = False
        elif going_down:
            if cur_N < N: ## P1. 등호 위치
                move_size /= 2
                cable_size -= move_size
            elif cur_N >= N:
                move_size /= 2
                cable_size += move_size
                going_down = False
                going_up = True
        if move_size == 1:
            for a in range(-1,2,1):
                answer.append([int(cable_size+a),get_cur_N(cable_size+a,K)])
                answer = sorted(answer,key = lambda x: (x[1],-x[0]))
            for i in range(len(answer)):
                if answer[i][1] >= N:
                    print(answer[i][0])
                    break
            break




    

    