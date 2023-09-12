'''
[BOJ] 15657. N과 M (8)
T: 1s
M: 512MB
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
ans = list()

def back():
    if (len(ans) == m) and ans==sorted(ans):
        print(*ans)
        return
    if ans != sorted(ans):
        return
    for i in range(n):
        ans.append(arr[i])
        back()
        ans.pop()

back()