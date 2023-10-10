'''
[BOJ] 24416. 알고리즘 수업 - 피보나치 수 1
T: 1s
M: 512MB
'''
import sys
input = sys.stdin.readline

n = int(input())
accum = 0
def fib(n):
    global accum
    if (n == 1 or n == 2):
        accum += 1
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(n), n-2)