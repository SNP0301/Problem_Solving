import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))


arr.sort(key=lambda x: (x[0], x[1]))


for i in range(n):
    print(arr[i][0],arr[i][1])