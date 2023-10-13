'''
[BOJ] 1026. 보물
T: 2초
M: 128MB
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
answer = 0

a.sort(reverse=True)
b.sort()

for i in range(n):
    answer += a[i]*b[i]

print(answer)
