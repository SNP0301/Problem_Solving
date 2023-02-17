def Kaprekar(n:int):
    value = n
    while(n>0):
        value += n%10
        n = n//10
        
    return value

arr = []

for i in range(10001):
    arr.append(0)

for i in range(1,10001):
    value = i
    while(Kaprekar(value)<=10000):
        arr[Kaprekar(value)] = 1
        value = Kaprekar(value)

for i in range(1,10001):
    if(arr[i]==0):
        print(i)