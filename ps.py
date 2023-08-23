from itertools import combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
arr = []
for i in range(1,n+1):
    arr.append(str(i+1))

arr = list(combinations(arr,m))
comLen = len(arr)

cnt = 0
while True:
    if(comLen%10==0):
        cnt += 1
        comLen = comLen // 10
    else:
        print(cnt)
        break