'''
[BOJ] 11047. 동전 0
T: 1초
M: 256MB
'''
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = list()
answer = 0

for _ in range(n):
    coins.append(int(input()))

for i in range(n-1,-1,-1):
    answer += k//coins[i]
    k -= (k//coins[i])*coins[i]

print(answer)