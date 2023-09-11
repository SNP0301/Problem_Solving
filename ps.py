'''
[BOJ] 3085. N과 M (4)
T: 1초
M: 128MB
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list()
answer = 0

for _ in range(n):
    arr.append(list(map(str,input().strip())))
    


def swap_y_forward(x,y):
    if y+1 >= n:
        return
    else:
        arr[x][y], arr[x][y+1] = arr[x][y+1], arr[x][y]

def swap_y_backward(x,y):
    if y+1 >= n:
        return
    else:
        arr[x][y+1], arr[x][y] = arr[x][y], arr[x][y+1]

def swap_x_forward(x,y):
     if x+1 >= n:
         return
     else:
         arr[x][y], arr[x+1][y] = arr[x+1][y], arr[x][y]

def swap_x_backward(x,y):
    if x+1 >= n:
        return
    else:
        arr[x+1][y], arr[x][y] = arr[x][y], arr[x+1][y]

def check_row(x):
    x_max = 0
    current = 1
    for k in range(n-1):
        if arr[x][k] == arr[x][k+1]:
            current += 1
        else:
            current = 1
        x_max = max(x_max,current)
    return x_max

def check_column(y):
    y_max = 0
    current = 1
    for k in range(n-1):
        if arr[k][y] == arr[k+1][y]:
            current += 1
        else:
            current = 1
        y_max = max(y_max,current)
    return y_max

for i in range(n):
    for j in range(n):
        swap_y_forward(i,j)
        answer = max(answer, check_row(i))
        answer = max(answer,check_column(j))
        if j+1 < n:
            answer = max(answer,check_column(j+1))

        swap_y_backward(i,j)

        swap_x_forward(i,j)
        answer = max(answer,check_column(j))
        answer = max(answer, check_row(i))
        if i+1 < n:
            answer = max(answer, check_row(i+1))
        swap_x_backward(i,j)

print(answer)