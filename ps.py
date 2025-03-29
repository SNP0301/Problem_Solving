"""
할 수 있다

[I/O]
    I: SCV의 수 1<=N<=3
        둘째 줄에는 SCV N개의 체력이 주어진다
    O: 모든 SCV를 파괴하기 위한 공격횟수의 최솟값


"""
def recur(x,y,z): 
    if (x,y,z) in acc: return acc[(x,y,z)]
    if (x,y,z) == (0,0,0): return
    
    cur_ans = min(recur(max(x-1,0),max(y-3,0),max(z-9,0)),\
                  recur(max(x-3,0),max(y-1,0),max(z-9,0)),\
                  recur(max(x-1,0),max(y-9,0),max(z-3,0)),\
                    recur(max(x-9,0),max(y-1,0),max(z-3,0)),\
                        recur(max(x-9,0),max(y-3,0),max(z-1,1)),\
                            recur(max(x-3,0),max(y-9,0),max(z-1,1)))
    
    acc[(x,y,z)] = cur_ans + 1
    return cur_ans +1

N = int(input())
scvs = list(map(int,input().split()))
scvs.extend([0]*(3-N))

acc = dict()


