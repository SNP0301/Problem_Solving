"""
[복잡도] O(n)
    - 학생들의 수 <= 1000인 자연수
    - 반대로 정렬([5,4,3,2,1])된 경우여도 
"""

N = int(input())
stdnts = list(map(int,input().split()))
#stk = [stdnts.pop(0)]
stk = []
turn = 1

while stdnts or stk:
    #print(stdnts,stk)
    if stdnts:
        if stdnts[0] == turn:
            stdnts.pop(0)
            turn += 1
        elif stdnts[0] != turn:
            if stk and stk[-1] == turn:
                stk.pop()
                turn += 1
            elif stk and stk[-1] != turn:
                stk.append(stdnts.pop(0))
            elif not stk:
                stk.append(stdnts.pop(0))
    elif not stdnts:
        if stk and stk[-1] != turn:
            break
        if stk and stk[-1] == turn:
            stk.pop()
            turn += 1
            #print(stk)

if not stk and not stdnts:
    print("Nice")
else:
    print("Sad")
    