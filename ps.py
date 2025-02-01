"""
[복잡도] O(n)
    - 명령의 수 N (1 <= N <= 2000000)만큼 연산
"""
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
my_deque = deque()

for _ in range(N):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        my_deque.append(cmd[1])
    elif cmd[0] == 2:
        my_deque.appendleft(cmd[1])
    elif cmd[0] == 3:
        if my_deque:
            print(my_deque.pop())
        elif not my_deque:
            print(-1)
    elif cmd[0] == 4:
        if my_deque:
            print(my_deque.popleft())
        elif not my_deque:
            print(-1)
    elif cmd[0] == 5:
        print(len(my_deque))
    elif cmd[0] == 6:
        if not my_deque:
            print(1)
        elif my_deque:
            print(0)
    elif cmd[0] == 7:
        if my_deque:
            print(my_deque[-1])
        elif not my_deque:
            print(-1)
    elif cmd[0] == 8:
        if my_deque:
            print(my_deque[0])
        elif not my_deque:
            print(-1)