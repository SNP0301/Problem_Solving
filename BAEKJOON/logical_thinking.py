N = int(input())
cnt = 0

for i in range(1,N+1):
    if(i<100):
        cnt += 1
    else:
        c = i//100
        t = (i//10)%10
        o = i%10
        if((c-t)==(t-o)):
            cnt += 1

print(cnt)