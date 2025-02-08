"""
* 팀 스터디
[복잡도] 

[구상]
    I: 잉크 문자열의 크기 I, 맵의 크기 N, 커맨드의 길이 K
        - 잉크 문자열
        - N*N 사이즈의 스테이지
        - K개의 커맨드 (공백 없음)
    O: N*N 사이즈의 스테이지 최종 모습
        - 사각형은 "@", 빈칸은 ".", 염색되지 않은 장애물은 "#", 염색된 장애물은 염색 잉크 알파벳 (대문자)

[고려사항]
    - y행 x열
    - 이동
        - 움직이는 물체 이름이 사각형, "@"로 표현.
        - 밖으로 벗어나거나 이동하려는 칸에 장애물이 있으면 해당 커맨드 무시
    - 잉크 충전
        - j가 들어오면 잉크 양 += 1
    - 점프
        - J가 들어오면
            1) "제자리에서" 점프
            2) 사각형이 가진 잉크 양만큼 범위 내의 "장애물"에 잉크를 뿌린다
                - 색상은 지금 써야 하는 잉크 색상
                - 범위는 abs(sx-x)-abs(sy-y) <= 잉크 양을 만족하는 x,y
                - 잉크 양은 0이 된다
                - 잉크 색상은 점프 커맨드 입력 횟수에 의해 정해진다
                    - (점프횟수)%잉크문자열 길이
                        R -> G -> B -> R -> G -> B -> R -> ...

"""
from collections import deque

def my_print(a):
    for x in a:
        print(x)
    print()

I, N, K = map(int,input().split())
my_ink = deque(input())
stage = [list(input()) for _ in range(N)]
commands = deque(input())

ix = 0
iy = 0
ink_amnt = 0
found = False
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(N):
    for y in range(N):
        if stage[x][y] == "@":
            ix, iy = x, y
            found = True
            break
    if found:
        break

while commands:
    cur_cmd = commands.popleft()

    if cur_cmd == 'j':
        ink_amnt += 1

    elif cur_cmd == "J":
        for x in range(N):
            for y in range(N):
                if abs(ix - x) + abs(iy - y) <= ink_amnt:
                    if stage[x][y] != "." and stage[x][y] != "@":
                        stage[x][y] = my_ink[0]
        my_ink.append(my_ink.popleft())
        ink_amnt = 0

    elif cur_cmd in ["U","D","L","R"]:
        if cur_cmd == "U":
            if 0<=ix-1<N and stage[ix-1][iy] == ".":
                stage[ix][iy] = "."
                ix -= 1
                stage[ix][iy] = "@"
        elif cur_cmd == "D":
            if 0<=ix+1<N and stage[ix+1][iy] == ".":
                stage[ix][iy] = "."
                ix += 1
                stage[ix][iy] = "@"
        elif cur_cmd == "L":
            if 0<=iy-1<N and stage[ix][iy-1] == ".":
                stage[ix][iy] = "."
                iy -= 1
                stage[ix][iy] = "@"
        elif cur_cmd == "R":
            if 0<=iy+1<N and stage[ix][iy+1] == ".":
                stage[ix][iy] = "." 
                iy += 1
                stage[ix][iy] = "@"
        
for x in stage:
    for y in x:
        print(y,end="")
    print()