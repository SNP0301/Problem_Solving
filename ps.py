'''
[BOJ] 27959. 초코바
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

if n*100 >= m:
    print("Yes")
else:
    print("No")