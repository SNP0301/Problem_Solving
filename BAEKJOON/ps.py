n = int(input())
space_n = n-1
for i in range(2*n-1):
    if(i<n):
        for j in range(space_n):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        space_n -= 1
        print("\n",end="")
    elif(i>=n):
        space_n += 1
        for j in range(space_n+1):
            print(" ",end="")
        for j in range(2*n-2*space_n-3):
            print("*",end="")
        print("\n",end="")
        