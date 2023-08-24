import sys
input = sys.stdin.readline

a,b = map(int,input().split())
m = int(input())
arr = list(map(int,input().split()))

decimalNumber = 0
multiNumber = 1
beforeBaseNumber = a
afterBaseNumber = b

for i in range(m-1,-1,-1):
    decimalNumber += multiNumber * arr[i]
    multiNumber *= a

print(decimalNumber)

while(beforeafterBaseNumber >= 0)