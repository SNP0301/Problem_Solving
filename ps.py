'''
[BOJ] 15652. N과 M (4)
T: 1s
M: 512MB
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m = map(int,input().split())
ans = list()

def back():
    if (len(ans) == m) and ans==sorted(ans):
        print(*ans)
        return
    if ans != sorted(ans):
        return
    for i in range(1,n+1):
        ans.append(i)
        back()
        ans.pop()

back()