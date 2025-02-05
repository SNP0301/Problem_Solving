"""
* 스터디
[복잡도] O(N**2)
    - 3000*3000의 사진에 대해 완전탐색

[구상]
    - 유성 탐색
        - 유성인 칸을 모두 알아내서, 유성의 초기 위치를 queue에 저장
            - 유성을 찾는 4방향 탐색 중 [x+1][y]가 "."인 곳을 만나면 땅 탐색 시작
        - 땅("#")인 곳을 찾아내면 answer_photo에 땅("#") 표시
    - 최소 간격 측정
        - 유성 탐색으로부터 시작
        - cnt=0으로 시작해, x값을 1씩 늘리면서 "#"을 만날 때까지 cnt += 1
        - return cnt 후, return 받은 cnt를 현재의 땅<->유성 최소거리와 비교해 최소값 갱신
    - 사진 출력
        - answer_photo를 R*S 사이즈의 "."로 선언
        - photo를 돌며 "X"인 좌표가 나오면

[시도]
    - 1트 (89603508): 시간 초과 -> sys.stdin.readline 추가
    - 2트 (89603683): 시간 초과 -> 진짜진짜 중요한 문제 = BFS 써야 할 것 "같아서" BFS 쓰는 것. 유성 탐색을 BFS로 할 이유가 1도 없었다.
                                    ㄴ 땅-유성 간 갭을 확인할 때는 [x+1][y]이 "."인 "X"에 대해서만 계산하면 된다. 매 X 볼 때마다 BFS하면 터지는 것은 당연함
                                    ㄴ "같아서"를 줄이자.
    - 3트 (89604067): 메모리 초과 -> answer_photo 안 쓰고 X 옮기기
                                    ㄴ 3000*3000을 두개 만들려고 했을 때 멈췄어야 함.
    - 4트 (89604500): 시간 초과 -> 사실 BFS를 딱 한번만 쓸 수 있었다. visited도 빼고 "."으로 표시했으면 됐다.
    - 5트 (89605172): 시간 초과 -> 한번만 쓸 수 있다고 해놓고 break 안 걸었다.

* 적어도 한 줄 이상의 공기가 존재
** 사진의 맨 밑줄은 모두 땅 -> 땅 탐색 시 무조건 땅을 발견할 수 있다는 보장
[] 문제 읽기 -> [] I/O 확인 -> [] 제약조건/특이사항 확인 -> [] 구상 -> [] 복잡도 계산 -> [] 손 구현 -> [] 구현 -> [] 오픈테케 -> []히든테케
"""
from collections import deque
import sys
input = sys.stdin.readline


def gap_search(x,y):
    cnt = 0
    while photo[x+1+cnt][y] != "#":
        if cnt > gap_mn:
            break
        cnt += 1
    return cnt


R, S = map(int,input().split())
photo = [list(input()) for _ in range(R)] 
comet = list() ## 유성 위치를 담는 리스트                                
gap_mn = 3000 + 1


for x in range(R):
    for y in range(S):
        if photo[x][y] == "X":
            comet.append((x,y))
            if photo[x+1][y] == ".":
                cur_gap = gap_search(x,y)
                if cur_gap < gap_mn:
                    gap_mn = cur_gap
            photo[x][y] = "."

while comet:
    x,y = comet.pop()
    photo[x+gap_mn][y] = "X"


for x in photo:
    for y in x:
        print(y,end="")