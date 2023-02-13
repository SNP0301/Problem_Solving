import sys

t = int(input())
for i in range(1, t+1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(a+b)

print(a)