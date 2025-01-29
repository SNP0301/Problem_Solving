"""
* 1 <= N <= 1000000
** Range = 2*10**9+1
"""
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
chk_lst = sorted(list(set(lst)))
dct = dict()
cnt = 0

for i in chk_lst:
    dct[i] = cnt
    cnt += 1

for i in range(len(lst)):
    print(dct[lst[i]],end=" ")








