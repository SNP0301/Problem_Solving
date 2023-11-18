'''
[BOJ] 2475. 검증수
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

a,b,c,d,e = map(int,input().split())

print((a**2+b**2+c**2+d**2+e**2)%10)