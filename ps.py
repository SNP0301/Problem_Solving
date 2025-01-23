T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    answer = list()
    score = 0
    if N == M:
        for i in range(N):
            score += a[i]*b[i]
        answer.append(score)
        score = 0
    elif N > M:
        for i in range(N-M+1):
            for j in range(M):
                score += a[i+j]*b[j]
            answer.append(score)
            score = 0
    elif N < M:
        for i in range(M-N+1):
            for j in range(N):
                score += a[j]*b[i+j]
            answer.append(score)
            score = 0
    else:
        print("?")


    ##print(answer)
    print("#%d %d"%(test_case, max(answer)))
    # ///////////////////////////////////////////////////////////////////////////////////