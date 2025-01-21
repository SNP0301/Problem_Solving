N = int(input())

dp = [-1]*(N+1)
answer = -1

numbers = [-1]
for _ in range(N):
    numbers.append(float(input()))

""" 메모리 초과 -> 바로 2차원 배열을 만들 이유가 없었다.
dp = [[0 for _ in range(N)] for _ in range(N)]
answer = -1

for i in range(N):
    dp[i][i] = numbers[i]

for i in range(N):
    for j in range(i+1, N):
        dp[i][j] = dp[i][j-1]*numbers[j]
        answer = max(answer,dp[i][j])
"""
for i in range(1, N+1):
    if dp[i-1] > 1:
        dp[i] = dp[i-1] * numbers[i]
    else:
        dp[i] = numbers[i]
    answer = max(answer,dp[i])

print('%.3f'%answer)