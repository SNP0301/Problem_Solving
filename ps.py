'''
[BOJ] 1003. 피보나치 함수
T: 0.25 s
M: 128 MB
'''
import sys
input = sys.stdin.readline


zero_call = [1,0]
one_call = [0,1]

for i in range(2,41):
    zero_call.append(zero_call[i-1]+zero_call[i-2])
    one_call.append(one_call[i-1]+one_call[i-2])

t = int(input())

for _ in range(t):
    n = int(input())
    print(zero_call[n], one_call[n])