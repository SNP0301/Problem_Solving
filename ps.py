'''
[BOJ] 1699. 제곱수의 합
T: 2s
M: 128MB
'''
import sys
input = sys.stdin.readline


MAX_IDX = 100000
n = int(input())

dp = [1]+[999]*(MAX_IDX+1)

perfect_number = [i*i for i in range(int(100000**0.5))]

def square_check(num):
    if num == int(num**0.5)**2:
        return True
    else:
        return False

for i in range(2,n+1):
    cnt = 1

    if square_check(i):
        dp[i] = 1
        '''
            while cnt*i <= n:
            dp[i*cnt] = min(dp[i*cnt],cnt)
            cnt += 1
        '''

    else:
        for x in perfect_number:
            dp[i] = min(dp[x] + dp[i-x],dp[i])
            
print(dp[n])