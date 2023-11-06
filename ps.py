'''
[BOJ] 2576. 홀수
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

odd = list()

for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        odd.append(n)

if not odd:
    print(-1)
else: 
    print(sum(odd))
    print(min(odd))
