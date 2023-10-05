'''
[BOJ] 1912. 연속합
T: 1s
M: 128MB

dp[i][j]의 의미: 
'''
import sys
input=sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
  data[i] = max(data[i], data[i] + data[i-1])
  
print(max(data))