'''
[BOJ] 10989. 수 정렬하기 3
T: 5초
M: 8MB
'''
import sys
input = sys.stdin.readline

num_arr = [0 for _ in range(10001)]

n = int(input())
for _ in range(n):
    num_arr[int(input())] += 1

for i in range(10001):
    if num_arr[i] != 0:
        for j in range(num_arr[i]):
            print(i)
