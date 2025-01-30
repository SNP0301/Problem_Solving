"""
* 지뢰가 열렸거나, 안 열렸거나

bomed 없애고 cnt 표시 이하에 지뢰 표시해도 틀리는 이유: 이미 이전에 탐색했지만 터지지 않았던 지뢰가 표시되지 않는다.
"""
def my_print(i):
    for x in i:
        print(x)
    print()

N = int(input())
original_arr = list()
played_arr = list()
answer_arr = [["." for _ in range(N)] for _ in range(N)]
bombed = False

dx = [0,-1,0,1,1,1,0,-1,-1]
dy = [0,1,1,1,0,-1,-1,-1,0]


for _ in range(N):
    original_arr.append(list(input()))
for _ in range(N):
    played_arr.append(list(input()))



for x in range(N):
    for y in range(N):
        cnt = 0
        if played_arr[x][y] == "x":
            for n in range(9): # n of nine
                nx = x + dx[n]
                ny = y + dy[n]
                if 0<=nx<N and 0<=ny<N:
                    if original_arr[nx][ny] == "*":
                        cnt += 1
            answer_arr[x][y] = cnt
            if original_arr[x][y] == "*":
                bombed = True
                answer_arr[x][y] = "*"

if bombed:
    for x in range(N):
        for y in range(N):
            if original_arr[x][y] == "*":
                answer_arr[x][y] = "*"


for x in range(N):
    for y in range(N):
        print(answer_arr[x][y],end="")
    print()