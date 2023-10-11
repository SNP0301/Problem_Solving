'''
[BOJ] 27433. 팩토리얼 2
T: 1s
M: 1024MB
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, k = map(int,input().split())
a = list(map(int,input().split()))

print(a)

def merge_sort(arr,p,r):
    if arr[p] < arr[r]:
        q = (p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)

def merge(arr,p,q,r):
    i = p
    j = q+1
    t = 1
    tmp = [0 for _ in range(r)]
    while (i<=q and j <= r):
        if (arr[i]<=arr[j]):
            tmp[t] = arr[i]
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1
    while (i<=q):
        tmp[t] = arr[i]
        i += 1
    while (j <= r):
        tmp[t] = arr[j]
        j += 1
    i = p
    t = 1
    while (i <= r):
        arr[i] = tmp[t]
        i += 1
        t += 1
