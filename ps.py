'''
[BOJ] 1764. 듣보잦ㅂ
T: 2s
M: 256MB
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d_set = set()
b_set = set()

for _ in range(n):
    d_set.add(input())
for _ in range(m):
    b_set.add(input())

db_set = d_set.intersection(b_set)
db_list = list(db_set)
db_list.sort()
print(len(db_list))
for i in db_list:
    print(i,end="")

