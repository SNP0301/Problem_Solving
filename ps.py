'''
[BOJ] 2529. 부등호
T: 1s
M: 256MB
'''
import sys
input = sys.stdin.readline
MAX_IDX = 5

k = int(input())
sign = list(input().split())
num_list = [i for i in range(0,MAX_IDX)]


## index:int, 채워야 할 자리수
## num_list:list, 사용할 수 있는 숫자들의 배열


def recur(idx:int, numbers:list, answer:int):
    if idx > k:
        print(answer)
    else:
        print(idx)


recur(0,num_list,0)