'''
[BOJ] 1075. 나누기
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

n = int(input())//100*100
n_last_two_digit = str(n)[-2:]
f = int(input())
answer = 0
for i in range(100):
    if (i+n)%f == 0:
        if i<= 9:
            print('0'+str(i))
        else:
            print(i)
        break