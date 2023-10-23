'''
[BOJ] 5532. 방학 숙제
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a%c == 0:
    k = a//c
else:
    k = a//c+1

if b%d == 0:
    m = b//d
else:
    m = b//d+1

print(l-max(k,m))