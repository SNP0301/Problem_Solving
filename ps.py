'''
[BOJ] 11052. 카드 구매하기
T: 1초
M: 256MB
'''
import sys
input = sys.stdin.readline

n = int(input())
card_pack = [0]+ list(map(int,input().split()))
dp = [0] * (n+1)

for i in range(n+1):
    for j in range(n+1):
        if j-i >= 0:
            dp[j] = max(dp[j],dp[j-i]+card_pack[i])

print(dp[n])