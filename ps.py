'''
[BOJ] 1436. 영화감독 숌
T: 2 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

n = int(input())
jm = ['0']
number = 666
def isDoom(x):    
    x_str = str(x)
    x_len = len(x_str)
    cnt = 0
    if x_len < 3:
        return False
    else:
        while cnt+3 <= x_len:
            if int(x_str[cnt:3+cnt]) == 666:
                return True
            else:
                cnt += 1


while True:
    if isDoom(number):
        jm.append(number)
        #print(jm)
    
    number += 1
    if n == len(jm)-1:
        print(jm[-1])
        break