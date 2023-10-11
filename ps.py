'''
[BOJ] 4779. 칸토어 집합
T: 1s
M: 128MB
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def cantorian(arr):
    if (len(arr) == 1):
        print(*arr,end="")
        #print("arr = ",arr)
        return
    tres = len(arr)//3
    for i in range(len(arr)):
        if i >= tres and i < tres*2:
            arr[i] = " "

    cantorian(arr[:tres])
    cantorian(arr[tres:tres*2])
    cantorian(arr[tres*2:])


for _ in range(4):
    n = int(input())
    if n == 0:
        print("-")
    else:
        arr = ["-" for _ in range(3**n)]
        cantorian(arr)
        #cantorian(arr)
        #print(*arr)
        print("\n")