'''
[BOJ] 14500. 테트로미노

1. Blue: 2가지
2. Yellow: 1가지
3. Orange: 8가지
4. Green: 4가지
5. Pink: 4가지
'''

import sys
input = sys.stdin.readline

n,m= map(int,input().split())
arr= []
for i in range(n):
    arr.append([int(x) for x in input().split()])

print(arr)