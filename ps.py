T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    answer = 0
    N, K = map(int,input().split())
    arr = list()

    for _ in range(N):
        arr.append(list(map(int,input().split())))

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    answer += 1
                cnt = 0
        if cnt == K:
            answer += 1
    zipped_arr = list(zip(*arr))
    for i in range(N):
        cnt = 0
        for j in range(N):
            if zipped_arr[i][j] == 1:
                cnt += 1
            elif zipped_arr[i][j] == 0:
                if cnt == K:
                    answer += 1
                cnt = 0

        if cnt == K:
            answer += 1



    print("#%d %d"%(test_case,answer))
    # ///////////////////////////////////////////////////////////////////////////////////