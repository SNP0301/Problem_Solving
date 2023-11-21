'''
[BOJ] 27918. 탁구 경기
T: 1 s
M: 1024 MB
'''

import sys
input = sys.stdin.readline

n = int(input())
d = 0
p = 0

for _ in range(n):
    s = input().rstrip()
    if s == 'D':
        d += 1
    elif s == 'P':
        p += 1
    if d-p >= 2:
        print("%d:%d"%(d,p))
        exit()
    elif p-d >= 2:
        print("%d:%d"%(d,p))
        exit()

print("%d:%d"%(d,p))