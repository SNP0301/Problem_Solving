"""
* 무조건 수요일 전에 다시 풀어보기
[복잡도] O(NlgN)
    - 너비는 N, 깊이는 M이 결정?

[구상]
    I: 회의의 수 1<=N<=100_000
        - N+1줄까지 회의의 정보: 시작 시간과 끝 시간은 0<=t<=2**31-1
    O: 사용할 수 있는 회의의 최대 갯수
    - 회의의 수 <= 100_000이면 내가 쓰던 방식으로는 불가능
        * 즉, 모든 회의를 고려하지 않고도 푸는 방법이 있을 것이다
    - 시작이 같은데 끝이 다르거나, 끝이 다른데 시작이 다른 것들 관리 필요
    - 어떻게 다 100_000개를 다 돌리지 않고도 최소 개수를 셀 수 있지?
        - 일단 박치기
    - 시작 시간이 같은 회의는, 끝 시간이 짧은 것만 유효하다.
        - 입력 받을 때부터 시작 시간이 같은데 끝 시간이 더 긴 입력이 들어오면 포함하지 말자
        - 따라서 시작 시간 1개당 1개의 회의만 유효하므로 dict로 입력 받고 관리 가능
            - room_dct[시작 시간] = 끝 시간
        - 근데 시작 시간과 끝 시간이 같은 경우 시작하자마자 끝난거라 같은 시간에 시작하는 다른 회의랑 병행 가능

* 회의의 시작 시간과 끝나는 시간이 같을 수도 있다 => 이 경우 시작하자마자 끝나는 것으로 간주

[테스트 케이스]
---
2
0 0
1 1
---
2
0 1
1 2
---
3
0 2
0 1
1 2
---
"""
from collections import defaultdict,deque
N = int(input())
room_dct = defaultdict(lambda : 2**31)  ## 회의 시간의 최대값이 2**31-1이므로 초기값을 2**31로 선언
room_lst = list()
s_equal_to_e = set()
answer = 0

for _ in range(N):
    s,e = map(int,input().split())
    if s == e:
        s_equal_to_e.add(s)             ## 시작 = 끝인 경우 dct에 안 넣고 따로 관리 => 얘만 들어오면?
    elif room_dct[s] > e:
        room_dct[s] = e                 ## 시작 시간을 key 값으로 두고, key 값이 같으면 종료 시간이 가장 짧은 것만 value로 남긴다

if room_dct:
    for s in room_dct:
        room_lst.append([s,room_dct[s]])    ## [s,e] 쌍을 담아 시작시간을 room_lst[순서][0], 끝시간을 room_lst[순서][1]로 관리
    room_lst.sort(key = lambda x: (x[0],x[1])) ## 뭐가 더 중요하지? => 

    cur_e = room_lst[0][1]          ## 일단 가장 빨리 시작하는 회의를 넣고 끝난 시간을 초기화
    answer = 1                      ## 넣었으니까 회의 수 = 1로 시작

    for r in room_lst[1:]:          ## 전체 회의에 대해 O(N)

        if r[0] >= cur_e:           ## 1) 지금 잡은 회의 끝나고 시작할 수 있는 애면 (시작=끝인 회의면 바로 시작&끝이므로 등호 추가)
            cur_e = r[1]
            answer += 1             ## 해당 회의 추가하고, 끝나는 시간 갱신
            if r[0] in s_equal_to_e:    ## 만약 시작=끝인 회의가 있던 타임이라면
                answer += 1             ## 하나 더 추가

        elif r[1] < cur_e:          ## 2) 지금 잡은 회의보다 더 일찍 끝나는 애면
            cur_e = r[1]            ## 지금 잡은 회의 캔슬하고 끝나는 시간 갱신 => 캔슬하고 r을 새로 잡은거니까 횟수 변경 x

    print(answer)

else:
    print(len(s_equal_to_e))

