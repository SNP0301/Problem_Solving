'''
[BOJ] 2193. 이친수
T: 2s
M: 128MB
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
num_array = list()

def get_pinary_number(x):
    if(len(x)>=n):
        num_array.append(x)
        return
    if(x[-1]=='0'):
        get_pinary_number(x+'1')
        get_pinary_number(x+'0')
    elif(x[-1]=='1'):
        get_pinary_number(x+'0')
    

get_pinary_number('1')
print(len(num_array))
