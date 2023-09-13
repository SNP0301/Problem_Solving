'''
[BOJ] 14226. 이모티콘
T: 2초
M: 512MB

## 2 takes 2s: copy + paste
## 4 takes 4s: copy + paste + copy + paste
## 6 takes 5s: copy + paste + copy + paste + paste
## 18 takes 8s: copy + paste + copy + paste + copy + paste + paste + paste

## copy에서 current_len 저장
## paste에서 current_len += copied_len
## -1에서 current_len 빼기
'''
import sys
input = sys.stdin.readline
from collections import deque

s = 18
MAX_INDEX = 20
sub_array = [i for i in range(10)]*2
time_array = [0 for _ in range(MAX_INDEX)]
time_array[1] = 1
current_length = 0
q = deque()


def check_array(array):
    for i in array:
        print(i)

def bfs(x):
    global current_length
    q.append(x)

    while q:
        x = q.popleft()
        dx = [current_length, x, -1] ## [0]: paste [1]: copy + paste [2]: -1
        print("x is %d, nextX are [%d, %d, %d]"%(x,x+dx[0],x+dx[1],x+dx[2]))
        for i in range(3):
            nextX = x + dx[i]
            if nextX >= MAX_INDEX or nextX <= 0:
                continue
            if time_array[nextX] == 0:
                if i == 0: 
                    time_array[nextX] = current_length + 1
                    q.append(nextX)
                    current_length = time_array[x]
                elif i == 1:
                    time_array[nextX] = current_length * 2
                    q.append(nextX)
                    current_length *= 2
                elif i == 2:
                    time_array[nextX] = current_length -1
                    q.append(nextX)
                    current_length -= 1
        print(time_array,"\n")

        

bfs(1)

##print(sub_array)
##print(time_array)

print(time_array[s])