'''
[BOJ] 10974. 모든 순열
T: 1s
M: 128MB
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())
input_arr = [i for i in range(1,n+1)]

def recur(answer_arr, set_arr):
    if len(answer_arr) == n:
        print(*answer_arr)
    
    else:
        for i in set_arr:
            if i in answer_arr:
                continue
            answer_arr.append(i)
            recur(answer_arr,set_arr)
            answer_arr.remove(i)

recur(list(),input_arr)

