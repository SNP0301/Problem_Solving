'''
[BOJ] 10773. 제로
T: 1초
M: 256MB
'''
import sys
input = sys.stdin.readline

k = int(input())

jb = list()

for _ in range(k):
    num = int(input())
    if num == 0:
        jb = jb[:-1]
    else:
        jb.append(num)

print(sum(jb))