'''
[BOJ] 1912. 연속합
T: 1s
M: 128MB
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = list(map(int,input().split()))
dp = list()

dp.append(arr)

## i: 1,2,3,...,n-1
answer = -99999
cnt = 2
for i in range(1,n):
    dp.append([])
    for j in range(n-i):
        ##print(i,j,dp[i-1][j],arr[j+cnt-1])
        dp[i].append(dp[i-1][j]+arr[j+cnt-1])
    cnt += 1
    answer = max(answer,max(dp[i]))

print(max(answer,max(arr)))