import sys
input = sys.stdin.readline

primeArr = [True]*1000005

for i in range(3,1000005,2):
    if primeArr[i]:
        for j in range(i*i, 1000001, 2*i):
            primeArr[j] = False


def findFactor(n):
    for i in range(3, n, 2):
        if primeArr[i] and primeArr[n-i]:
            return "{0} = {1} + {2}".format(n, i, n-i)
    return "Goldbach\'s conjecture is wrong."

while True:
    n = int(input().rstrip())
    if(n==0):
        break
    else:
        print(findFactor(n))