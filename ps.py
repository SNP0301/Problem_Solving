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
answer_list = list()
## index:int, 채워야 할 자리수
## num_list:list, 사용할 수 있는 숫자들의 배열

def recur(idx:int, input_array:list, answer:int):
    numbers = input_array
    if idx >= k:
        answer_list.append(answer)
        return
    else:
        
        possible = False

        if sign[idx] == ">":
            for x in numbers:
                if answer%10 > x:
                    #print("after %d, %d is small"%(answer%10,x))
                    next_list = [i for i in numbers]
                    next_list.remove(x)
                    recur(idx+1, next_list, answer*10+x)
                    possible = True

        elif sign[idx] == "<":
            for x in numbers:
                if answer%10 < x:
                    #print("after %d, %d is large"%(answer%10,x))
                    next_list = [i for i in numbers]
                    next_list.remove(x)
                    recur(idx+1, next_list, answer*10+x)
                    possible = True

        if not possible:
            return


for i in range(MAX_IDX):
    first_list = [i for i in range(0,MAX_IDX)]
    first_list.remove(i)
    recur(0,first_list,i)

print(max(answer_list))

if sign[0] == "<":
    print("0"+str(min(answer_list)))
else:
    print(min(answer_list))