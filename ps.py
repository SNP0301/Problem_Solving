'''
[BOJ] 2455. 지능형 기차
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

h = list()
c = 0
for _ in range(4):
    d, u = map(int,input().split())
    c += u-d
    h.append(c)

print(max(h))
