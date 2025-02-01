"""
[복잡도] O(n)
    - 명령의 수 1,000,000
    - 명령당 연산/입출력 1~2
"""
import sys
input = sys.stdin.readline

N = int(input())
stk = []
for _ in range(N):
    cmd = list(map(int,input().split()))

    if cmd[0] == 1:
        stk.append(cmd[1])
    elif cmd[0] == 2:
        if stk:
            print(stk.pop())
        elif not stk:
            print(-1)
    elif cmd[0] == 3:
        print(len(stk))
    elif cmd[0] == 4:
        if stk:
            print(0)
        elif not stk:
            print(1)
    elif cmd[0] == 5:
        if stk:
            print(stk[-1])
        elif not stk:
            print(-1)
    else:
        print("???")