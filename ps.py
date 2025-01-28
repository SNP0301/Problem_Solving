n = int(input())

arr = [0,1,2,3] + [0 for _ in range(n-3)]

for i in range(4,n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[n]%10007)