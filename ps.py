import sys
input = sys.stdin.readline

def calculate(m,n,x,y):
    ans = x
    while ans <= m*n:
        if (ans-x)%m ==0 and (ans-y)%n==0:
            return ans
        ans += m
    return -1


t = int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())
    print(calculate(m,n,x,y))