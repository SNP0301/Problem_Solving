"""
* 스터디
[복잡도] O(N**2)
    - 5*5 배열에 대해 빙고 검사
        - 빙고 검사 1회마다 60개의 칸에 대해 연산


[구상]
    I: 빙고판에 적힌 수, 사회자가 부르는 수
    O: 사회자가 몇번째 수를 불렀을 때 철수가 빙고를 외치는지

* 선이 3개 이상 그어지는 순간 빙고를 외친다

[] 문제 읽기 -> [] I/O 확인 -> [] 제약조건/특이사항 확인 -> [] 구상 -> [] 복잡도 계산 -> [] 손 구현 -> [] 구현 -> [] 오픈테케 -> []히든테케
"""
from collections import deque

def count_bingo():
    cnt = 0
    for x in range(5):
        if sum(board[x]) == 0:
            cnt += 1
        if sum(zip_board[x]) == 0:
            cnt += 1
    
    bd_cnt = 0
    zbd_cnt = 0
    for i in range(5):
        if board[i][i] == 0:
            bd_cnt += 1
        if zip_board[i][4-i] == 0:
            zbd_cnt += 1

    if zbd_cnt == 5:
        cnt += 1
    if bd_cnt == 5:
        cnt += 1
    return cnt

def check_num(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
            if zip_board[i][j] == num:
                zip_board[i][j] = 0


board = [list(map(int,input().split())) for _ in range(5)]
zip_board = [list(tmp) for tmp in zip(*board)]
ment = deque()
num = 0
answer = 1

for _ in range(5):
    info = list(map(int,input().split()))
    for x in info:
        ment.append(x)

while ment:        
    num = ment.popleft()
    check_num(num)


    if count_bingo() >= 3:
        print(answer)
        break
    else:
        answer += 1