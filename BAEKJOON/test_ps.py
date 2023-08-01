import math

primeArr = []
primeArr.append(False)
primeArr.append(False)
primeArr.append(True)
for i in range(3,100005):
    isPrime = True
    for j in range(2,math.ceil(math.sqrt(i)+1)):
        if (i%j==0):
            primeArr.append(False)
            isPrime = False
            break
    if(isPrime==True):
        primeArr.append(True)


while True:
    n = int(input())
    if(n==0):
        break
    a = 3
    b = n-3
    isWrong = True
    while(a<=b):
        #print("for [%d, %d]: %r %r"%(a,b,primeArr[a],primeArr[b]))
        if((primeArr[a]==True)and(primeArr[b]==True)):
            print("%d = %d + %d"%(n,a,b))
            isWrong = False
            break
        else:
            a += 2
            b -= 2
    if(isWrong==True):
        print("Goldbach's conjecture is wrong.")