'''
[BOJ] 1699. 제곱수의 합
T: 2s
M: 128MB
'''
import sys
import math
input = sys.stdin.readline


MAX_IDX = 100000
n = int(input())

## 1,4,9,16 ... 
dp = [999]*(MAX_IDX+1)
check = [i for i in range(MAX_IDX)]
dp[1] = 1
current_dp = 1

for i in range(2,n+1):
    floor_number = math.floor(math.sqrt(i))
    basic_number = math.sqrt(i)

    if floor_number == basic_number:
        dp[i] = 1
        current_dp = i
        cnt = 1
        while cnt*i <= n:
            dp[i*cnt] = min(dp[i*cnt],cnt)
            cnt += 1
    else:
        dp[i] = min(dp[current_dp] + dp[i-current_dp],dp[i])

print(dp[n])