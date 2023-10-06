'''
[BOJ] 1158. 요세푸스 문제
T: 2s
M: 256MB
'''
import sys
input=sys.stdin.readline
from collections import deque

n, k = map(int,input().split())

people = deque([i for i in range(1,n+1)])

print("<", end="")
for _ in range(n-1):
    for _ in range(k-1):
        people.append(people.popleft())
    print(people.popleft(),end=", ")
print(people.popleft(),end=">")