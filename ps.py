"""
* 어림 잡아서라도 시간복잡도 계산해서 상단에 적어두기
    - 보통 반복문 크기로 본다
    - 시간초과 보고 나서 바꾸면 늦는다
    - nlogn과 n^2는 하늘과 땅 차이 -> 알고리즘으로 줄이든, 자구로 줄이든 줄일 수 있는 방법을 찾아라
"""
N = int(input())
lst = list(map(int,input().split()))
stk = [] ## stk[x][0] = 해당 탑의 위치, stk[x][1] = 해당 탑의 높이
answer = [0 for _ in range(N)]

for i in range(N):
    while stk: 
        if stk[-1][1] > lst[i]: ## top of stk이 현재 탑의 높이보다 크면 top of stk이 신호를 받아준다 
            answer[i] = stk[-1][0] + 1 ## 탑 위치는 0~n-1이므로 +1 해서 ans에 저장
            break
        else:
            stk.pop()
    stk.append([i,lst[i]]) ## 처음 for 문 들어왔을 때는 while stk:을 거치지 않으므로 바로 append

for i in answer:
    print(i,end=" ")
