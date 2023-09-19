'''
[BOJ] 14501. 퇴사
T: 2초
M: 512MB
'''
import sys
input = sys.stdin.readline

n = int(input())
time_table = list()
pay_table = list()
dp = [0] * (n+1)
max_value = 0

for i in range(n):
    time, pay = map(int,input().split())
    time_table.append(time)
    pay_table.append(pay)

for i in range(n-1,-1,-1):
    t = i + time_table[i]
    if t <= n:
        dp[i] = max(pay_table[i] + dp[t], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)