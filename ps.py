"""
[복잡도] O(lgN)?
    - 이분탐색은 input이 시행마다 지수승으로 줄어드니까?

[실수]
    1. 이미 계산했던 값을 사용해야 하는거면 arr가 맞지만, 하나의 값을 찾는데 다른 값이 영향을 주지 않는다면 arr를 선언할 필요는 없다.
        - 특히 이 문제에서 (2**15)*(2**15) arr를 사용하면 서버 터진다.
    2. 표가 나왔냐/안 나왔냐를 보고 배열을 짤게 아니고, 찾으려는 값이 어떤 값인지, 그 값이 이전 값의 영향을 받는지/안받는지, 순서가 정해진 목록 중 단일 값을 찾는 것인지를 먼저 살펴볼 것.

[배운 것]
    1. 함수를 완벽하게 짰다는 전제 하에 재귀함수에서 return 자기자신을 하면, 해당 함수에서 얻고자 하는 출력/값을 얻을 때까지 계산한다.
        - 예) 피보나치도 return fib 하면 자기가 호출했던 fib 결과를 모두 합쳐서 되돌려준다.
    2. 이분탐색 자체는 탐색 범위를 반으로 줄여가면서 탐색한다. 정렬된 배열에서 사용한다.
        - 정렬됐는가?: 이 문제는 값 자체가 정렬된 것은 아니지만 Z모양 탐색 순서가 변칙없이 정해져있다.
        - 반으로 줄일 수 있는가? : 주어진 표가 2**N 길이의 변만 가지므로 반으로 줄여가면서 탐색할 수 있다.
        - FTR) 랜선 자르기, 나무 자르기

[틀린 코드] - 메모리 메모리 메모리
import sys
sys.setrecursionlimit(10**6)


def my_print(a):
    for x in a:
        print(x)
    print()

def do_z(x,y,N,cur):
    if N == 1:
        for f in range(4): ## f of four
            nx = x+dx[f]
            ny = y+dy[f]
            answer[nx][ny] = cur
            cur += 1
    else:
        do_z(x,y,N-1,cur+2**(2*N-2)*0)
        do_z(x,y+2**(N-1),N-1,cur+2**(2*N-2)*1)
        do_z(x+2**(N-1),y,N-1,cur+2**(2*N-2)*2)
        do_z(x+2**(N-1),y+2**(N-1),N-1,cur+2**(2*N-2)*3)

N, r, c = map(int,input().split())
answer = [[0 for _ in range(2**N)] for _ in range(2**N)]
cur = 0
dx = [0,0,1,1]
dy = [0,1,0,1]

do_z(0,0,N,cur)
print(answer[r][c])
"""

import sys

N, r, c = map(int, sys.stdin.readline().split())

cur = 0
sz = 2 ** (N - 1)  ## N이 1일 때 1*1씩, 2일 때 2*2씩

while sz > 0: 
    cur_full_size = sz * sz  ## 지금 탐색하려는 범위 전체의 사이즈

    ## 2**(2*N-2)만큼 갔는데도 r,c각각 못 찾으면, 못 찾은 방향으로 2**(2*N-2) 만큼 이동
    if r < sz and c < sz:
        cur += cur_full_size * 0

    ## x는 아직 남았는데 y는 못 지나갔으면
    elif r < sz and c >= sz:
        cur += cur_full_size * 1
        c -= sz

    ## y는 아직 남았는데 x는 못 지나갔으면
    elif r >= sz and c < sz:
        cur += cur_full_size * 2
        r -= sz  

    ## 나머지 경우
    else:
        cur += cur_full_size * 3
        r -= sz
        c -= sz

    sz //= 2  # 크기를 절반으로 줄이면서 탐색

print(cur)
