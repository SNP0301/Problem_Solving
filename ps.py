'''
[BOJ] 1247. 부호
T: 2 s
M: 256 MB
'''

import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    cnt = 0
    for i in range(n):
        cnt += int(input())
    if cnt == 0:
        print(0)
    elif cnt < 0:
        print("-")
    else:
        print("+")