'''
[BOJ] 15988. 1,2,3 더하기 3
T: 1초
M: 512MB
'''
import sys
input = sys.stdin.readline

t = int(input())

dp = [0 for _ in range(1000002)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,1000001):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009

for _ in range(t):
    n = int(input())
    print(dp[n]%1000000009)