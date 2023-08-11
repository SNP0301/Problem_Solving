import sys
from collections import Counter
input = sys.stdin.readline
arr = []
accum = 0

for _ in range(10):
    num  = int(input())
    arr.append(num)
    accum += num

var = Counter(arr).most_common()


print(accum/10)
print(var)