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

def check_array(array):
    for i in array:
        print(i)

check_array(modified_array)

for i in range(x):
    original_array.append(modified_array[i][:w])


check_array(original_array)