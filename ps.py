from itertools import product
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr =[]

for i in range(1,n+1):
    arr.append(str(i))

pro_arr = product(arr,repeat=m)

for i in pro_arr:
    printable = True
    for j in range(len(i)-1):
        if(i[j] > i[j+1]):
            printable = False
            break
    if(printable == True):
        print(" ".join(i))
