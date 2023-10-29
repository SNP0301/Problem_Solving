'''
[BOJ] 10768. 특별한 날
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

m = int(input())
d = int(input())

if (m<2) or (m <=2 and d<18): 
    print("Before")
elif m==2 and d == 18:
    print("Special")
else:
    print("After")