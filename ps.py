'''
[BOJ] 2529. 부등호
T: 1s
M: 256MB
'''
import sys
input = sys.stdin.readline
MAX_IDX = 10 ## 453 342

k = int(input())
sign = list(input().split())
num_list = [i for i in range(0,MAX_IDX)]

## index:int, 채워야 할 자리수
## num_list:list, 사용할 수 있는 숫자들의 배열

def recur(idx:int, numbers:list, answer:int):

    if idx >= k:
        print(answer)
    
    else:
        possible = False

        if sign[idx] == ">":
            for x in numbers:
                if answer%10 > x:
                    next_list = numbers
                    next_list.remove(x)
                    recur(idx+1, next_list, answer*10+x)
                    possible = True

        elif sign[idx] == "<":
            for x in numbers:
                if answer%10 < x:
                    next_list = numbers
                    next_list.remove(x)
                    recur(idx+1, next_list, answer*10+x)
                    possible = True

        if not possible:
            return


for i in range(MAX_IDX):
    first_list = [i for i in range(0,MAX_IDX)]
    first_list.remove(i)
    print(i, first_list)
    recur(0,first_list,i)