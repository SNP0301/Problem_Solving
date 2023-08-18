from itertools import product
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

preArr = list(map(int,input().split()))
preArr.sort()

postArr = list(map(str,preArr))

perTuple = product(postArr,repeat=m)

printedArr = []

for i in perTuple:
    iList = sorted(list(i))
    ##print(iList)
    if iList not in printedArr:
        printedArr.append(iList)
        i = tuple(iList)
        print(" ".join(i))


