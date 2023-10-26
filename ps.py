'''
[BOJ] 5596. 시험 점수
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

m = sum(list(map(int,input().split())))
s = sum(list(map(int,input().split())))

print(max(m,s))