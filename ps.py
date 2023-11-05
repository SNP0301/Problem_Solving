'''
[BOJ] 11943. 파일 옮기기
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())


for _ in range(n):
    bread = input().strip()
    for i in range(len(bread)-1,-1,-1):
        print(bread[i],end="")
    print("")
