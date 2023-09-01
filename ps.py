import sys
input = sys.stdin.readline

n = int(input())
dong = list() ## works as a cnt
arr = list() ## works as a map

## def BFS(x,y):

for i in range(n):
    line = input().rstrip()
    print(line)
    arr.append([int(x) for x in line])

print(arr)
