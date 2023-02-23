N, M = map(int,input().split())
arr = []

for i in range(N+1):
    arr.append(i)

for k in range(M):
    i, j = map(int,input().split())
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

for i in range(1,N+1):
    print(arr[i],end=" ")