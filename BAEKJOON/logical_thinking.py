H, M = map(int,input().split())

if(M-45<0):
    if(H-1<0):
        H = 23
        M = 60 - (45 - M)
    elif(H-1>=0):
        H = H - 1
        M = 60 - (45 - M)
elif(M-45>=0):
    M = M - 45

print(H,M)