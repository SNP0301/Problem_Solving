from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list()

for i in range(1,n+1):
    arr.append(str(i))


for e in list(permutations(arr,m)):
    print(" ".join(e))