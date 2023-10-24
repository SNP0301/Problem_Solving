'''
[BOJ] 5554. 심부름 가는 길
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())

t = a+b+c+d

print(t//60)
print(t%60)