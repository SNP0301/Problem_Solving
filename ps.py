'''
[BOJ] 11726. 2*n 타일링
T: 1초
M: 256MB
'''

import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 2
l = 3

while dp[n] == 0:
    dp[l] = dp[l-1]+dp[l-2]
    l += 1

print(dp[n]%10007)