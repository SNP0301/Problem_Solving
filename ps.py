'''
[BOJ] 2752. 세수정렬
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

s = list(map(int,input().split()))
s.sort()

for i in s:
    print(i,end=" ")