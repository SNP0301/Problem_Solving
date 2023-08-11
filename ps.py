import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    inputArr = list(input().split())
    for j in range(1,4):
        inputArr[j] = int(inputArr[j])
    arr.append(inputArr)

arr.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))

for i in range(len(arr)):
    print(arr[i][0])