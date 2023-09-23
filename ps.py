'''
[BOJ] 10816. 숫자 카드 2
T: 1s
M: 256MB
'''
import sys
input = sys.stdin.readline

n = int(input())
input_list = list(map(int,input().split()))


plus_list = [0 for i in range(10000001)]
minus_list = [0 for i in range(10000001)]

for i in input_list:
    if i >= 0:
        plus_list[i] += 1
    else:
        minus_list[i] += 1

m = int(input())

for i in list(map(int,input().split())):
    if i >= 0:
        print(plus_list[i],end=" ")
    else:
        print(minus_list[i],end=" ")