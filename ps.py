'''
[BOJ] 11651. 좌표 정렬하기 2
T: 1초
M: 256MB
'''
import sys
input = sys.stdin.readline

n = int(input())

arr = list()

for _ in range(n):
    arr.append(list(map(int,input().split())))


arr.sort(key = lambda x: (x[1],x[0]))

for i in arr:
    print(i[0],i[1])