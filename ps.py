'''
[BOJ] 11365. !밀비 급일
T: 1 s
M: 256 MB
'''

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
c,d = map(int,input().split())

if b+c < a+d :
    print(b+c)
else:
    print(a+d)