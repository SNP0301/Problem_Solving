'''
[BOJ] 15990. 1,2,3 더하기 5
T: 1s
M: 512MB
'''
import sys
input=sys.stdin.readline

MAX_IDX = 100000

dp = [[0]*4 for _ in range(MAX_IDX+1)]

dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]

for i in range(4,MAX_IDX+1):
    dp[i][1] = dp[i-1][2] + dp[i-1][3]
    dp[i][2] = dp[i-2][1] + dp[i-2][3]
    dp[i][3] = dp[i-3][1] + dp[i-3][2]

    dp[i][1] %= 1000000009
    dp[i][2] %= 1000000009
    dp[i][3] %= 1000000009

t = int(input())
for _ in range(t):
    print(sum(dp[int(input())])%1000000009)