'''
[BOJ] 2193. 이친수
T: 2s
M: 128MB
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

pinary_number = [0,1,1,2]+[0 for _ in range(87)]
i = 3

while i <= n:
    pinary_number[i] = pinary_number[i-1]+pinary_number[i-2]
    i += 1

print(pinary_number[n])

