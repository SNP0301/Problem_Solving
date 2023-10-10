'''
[BOJ] 9461. 파도반 수열
T: 1s
M: 128MB
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

t = int(input())
dp = [0,1,1,1] + [0 for _ in range(99)]

for i in range(4,101):
    dp[i] = dp[i-2]+dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])