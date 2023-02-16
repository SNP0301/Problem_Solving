c = int(input())

for i in range(c):
    arr = list(map(int,input().split()))
    for j in range(arr[0]):
        cnt = 0
        length = len(arr)-1
        avg = (sum(arr)-arr[0])/length
        for k in range(1,length+1):
            if (arr[k]>avg):
                cnt += 1
    print('%.3f%c'%(cnt*100/length,"%"))
