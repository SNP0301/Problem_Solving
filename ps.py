'''
[BOJ] 14226. 이모티콘
T: 2초
M: 512MB
'''
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()

check_array = [i for i in range(10000)]
time_array = [i for i in range(10000)] ## time_array[n]: n개 이모티콘을 만드는 데에 걸리는 최소 시간
time = 1

i = 2
for j in range(n):
    for i in range(j,2*n+1,i):
        time_array[2*i] = time_array[i]+1 ## [4]는 [2]에서 2초, #
        print("%d takes %d"%(2*i,time_array[2*i]))

i = 2
for i in range(2,2*n):
    time_array[i] = min(time_array[i+1]+1, time_array[i])

print("\n")
print(time_array[n])