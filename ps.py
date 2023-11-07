'''
[BOJ] 1267. 핸드폰 요금
T: 2 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

y = 0
m = 0

for i in range(n):
    y += arr[i]//30+1
    m += arr[i]//60+1

if y*10 == m*15:
    print("Y M", y*10)
elif y*10 < m*15:
    print("Y", y*10)
else:
    print("M", m*15)



