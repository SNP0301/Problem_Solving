"""
[복잡도]
    - 20*20 크기의 보드에서 완전탐색 => 최악의 경우 한번 탐색할 때마다 

[구상]
    I: 표의 크기 1<=R,C<=20
        - R개의 줄에 걸쳐 C개의 대문자 알파벳
    O: 같은 알파벳이 적힌 칸을 두 번 지나지 않고 움직일 수 있는 최대의 칸 수
"""
def dfs(x,y,st,cur_alphabet):
    global answer
    if cur_alphabet in st:
        answer = max(answer,len(st))
        print(st)
        return
    else:
        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]
            if 0<=nx<R and 0<=ny<C and not v[nx][ny]:
                new_st = {i for i in st}
                new_st.add(cur_alphabet)
                v[nx][ny] = True
                dfs(nx,ny,new_st,arr[nx][ny])
                v[nx][ny] = False
                #new_st.remove(cur_alphabet)

R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
v = [[False for _ in range(C)] for _ in range(R)]
v[0][0] = True
answer = 0

dx = [1,0,0,-1]
dy = [0,1,-1,0]

for t in range(2):
    dfs(dx[t],dy[t],set(),arr[0][0])

print(answer)