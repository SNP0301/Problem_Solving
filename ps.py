'''
[BOJ] 1264. 모음의 개수
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    sen = input()
    print("%d."%(i+1),sen,end="")