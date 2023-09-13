'''
[BOJ] 16967. 배열 복원하기
T: 2s
M: 512MB
'''
import sys
input = sys.stdin.readline

h,w,x,y = map(int,input().split())

original_array = list()
modified_array = list()

for i in range(x+h):
    modified_array.append(list(map(int,input().split())))

for i in range(x):
    original_array.append(modified_array[i][:w])

for i in range(h-x):
    original_array.append([0 for _ in range(w)])

for i in range(h):
    for j in range(w):
        original_array[i][j] = modified_array[i][j]

for i in range(h-x):
    for j in range(w-y):
        original_array[i+x][j+y] -= original_array[i][j]


for i in original_array:
    print(*i)