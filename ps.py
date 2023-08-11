from itertools import product

arr = list()
n, m = map(int,list(input().split()))
for i in range(n):
    arr.append(str(i+1))

pro_arr = product(arr,repeat=m)

for i in pro_arr:
    printable = True
    for j in range(len(i)-1):
        if(i[j] > i[j+1]):
            printable = False
            break
    if (printable==True):
        print(" ".join(i))
    

