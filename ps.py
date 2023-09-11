'''
[BOJ] 1463. 1로 만들기
T: 0.15초
M: 128MB
'''
import sys
input = sys.stdin.readline

n = int(input())
MAX_INDEX = 1000000
dp = [0 for _ in range(MAX_INDEX*3+1)]

dp[1] = 0
dp[2] = 1
dp[3] = 1

l = 3

while l <= MAX_INDEX:
    if dp[l] == 0:
        if l % 3 == 0:
            dp[l] = dp[l//3] + 1
        elif l % 2 == 0:
            dp[l] = dp[l//2] + 1 
        else:
            dp[l] = dp[l-1] + 1

    if dp[l*3] == 0 or dp[l*3] > dp[l]:
        dp[l*3] = dp[l] + 1
    
    if dp[l*2] == 0 or dp[l*2] > dp[l]:
        dp[l*2] = dp[l] + 1
    
    if dp[l+1] == 0 or dp[l+1] > dp[l]:
        dp[l+1] = dp[l] + 1

    l += 1

print(dp[n])
