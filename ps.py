"""
- 가장 짧은 것부터 or 가장 긴 것부터 따지는거 아니고 알고리즘?
    - 왜?
- 최대한 많은을 구하고 시작?

[개인 복습]
    - 다른 문제 dx, dy할 때 while 안 썼을텐데?
    - 0b~~ 써서 가능?

"""


def connect_border (arr,N):
    for x in [0,N-1]:
        for y in range(N):
            if arr[x][y] == 1:
                arr[x][y] = -1
    for y in [0,N-1]:
        for x in range(N):
            if arr[x][y] == 1:
                arr[x][y] = -1
    return 1

T = int(input())
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = list()
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    ##print(arr)

    connect_border(arr,N)
    current_arr = arr
    possible_lst = list()

    for x in range(N):
        for y in range(N):
            if current_arr[x][y] == 1:
                possible_cnt = 0
                for d in range(4):
                    cnt = 1
                    while True:
                        nx = x + dx[d]*cnt
                        ny = y + dy[d]*cnt
                        if not(0<=nx<N and 0<=ny<N):
                            possible_cnt += 1
                            break
                        else:
                            cnt += 1
                            if current_arr[nx][ny] != 0:
                                break

                possible_lst.append([x,y,possible_cnt])
    possible_lst = sorted(possible_lst,key = lambda x: x[2])
    #possible_lst = get_possible_lst()
    for i in range(possible_lst):
        x = possible_lst[0][0]
        y = possible_lst[0][1]

        ### 동작하고

        possible_lst[0]

    print(possible_lst)


    print("#%d %d" % (test_case, answer))

    # ///////////////////////////////////////////////////////////////////////////////////