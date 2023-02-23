N, M = map(int,input().split())
arr= []

for i in range(N+1):
    arr.append(0)


for i in range(M):
    start, end, num = map(int,input().split())
    for j in range(start,end+1):
        arr[j]=num

for i in range(1,N+1):
    print(arr[i],end=" ")
        

