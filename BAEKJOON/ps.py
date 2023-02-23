N, M = map(int,input().split())
arr = []

for i in range(N+1):
    arr.append(i)

for k in range(M):
    i, j = map(int,input().split())
    cnt = 0
    for z in range((j-i+1)//2):
        tmp = arr[i+cnt]
        arr[i+cnt]=arr[j-cnt]
        arr[j-cnt]= tmp
        cnt+=1

for i in range(1, N+1):
    print(arr[i],end=" ")