'''
[BOJ] 20492. 세금
T: 1 s
M: 1024 MB
'''

import sys
input = sys.stdin.readline

n = int(input())

print(int(n*0.78), int(n*0.8)+int(n*0.2*0.78))