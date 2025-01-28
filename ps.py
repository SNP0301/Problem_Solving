"""
N = int(input())
answer = 0
while N != 1:
    if N%3 == 0:
        N = N//3
    elif (N-1)%3 == 0:
            N -= 1
    elif N%2 == 0:
        N = N//2
    else:
        N -= 1
    answer += 1
print(answer)

"""
N = int(input())
answer = [1000001 for _ in range(N+1)]
if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    answer[2] = 1
    answer[3] = 1

    for n in range(2,N+1):
        if n*3 <= N:
            answer[n*3] = min(answer[n*3],answer[n]+1)
        if n*2 <= N:
            answer[n*2] = min(answer[n*2],answer[n]+1)
        if n+1 <= N:
            answer[n+1] = min(answer[n+1],answer[n]+1)
    print(answer[N])
