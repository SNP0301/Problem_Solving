import sys
input = sys.stdin.readline

for _ in range(3):
    cnt = 0
    arr = [int(x) for x in input().split()]
    print(arr)
    for i in range(4):
        cnt += arr[i]
    if(cnt==4):
        print("E")
    elif(cnt==3):
        print("A")
    elif(cnt==2):
        print("B")
    elif(cnt==1):
        print("C")
    else:
        print("D")