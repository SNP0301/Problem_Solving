n = int(input())
list = list(map(int,input().split()))
min = 9999999
max = -9999999
for i in range(0,n):
    if (list[i]>=max):
        max = list[i]
    if (list[i]<=min):
        min = list[i]

print('%d %d'%(min, max))