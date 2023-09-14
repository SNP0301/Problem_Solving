'''
[BOJ] 10815. 숫자 카드
T: 2초
M: 256MB
'''

import sys
input = sys.stdin.readline

n = int(input())
sg_deque = set(input().split())
m = int(input())
check_deque = list(input().split())

for i in check_deque:
    if i in sg_deque:
        print(1, end=" ")
    else:
        print(0, end=" ")