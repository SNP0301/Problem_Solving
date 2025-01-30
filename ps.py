"""
"""

N, K = map(int,input().split())
arr = [[K-N+1,K-N+1,K-N+1] for _ in range(0,2*K+5)]
cur = 1
if N == K:
    print(0)
else:
    arr[K] = [0,0,0]
    arr[K*2] = [1,1,1]
    if N == 0:
        arr[N+1][0] = 1
    else:
        for i in range(K*2,N,-1):
            cur = min(arr[i])
            #print("%d goes to %d, %d, %d"%(i, i+1, i-1, i//2))
            arr[i+1][0] = min(min(arr[i+1]), cur + 1)
            arr[i-1][1] = min(min(arr[i-1]), cur + 1)
            arr[i//2][2] = min(min(arr[i//2]), cur + 1)

for i in range(N,2*K+2):
    print(i, arr[i])
    
