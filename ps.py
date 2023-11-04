'''
[BOJ] 9093. 단어 뒤집기
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    words = list(input().split())
    for i in words:
        for j in range(len(i)-1,-1,-1):
            print(i[j],end="")
        print(" ",end="")
    print()