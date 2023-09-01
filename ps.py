from collections import deque

import sys
input = sys.stdin.readline


n = int(input())
deque = deque()

for _ in range(n):
    command = list(map(str,input().split()))

    if(len(command)==2):
        X = int(command[1])

    if(command[0] == "push_front"):
        deque.appendleft(X)
    elif(command[0] == "push_back"):
        deque.append(X)
    elif(command[0] == "pop_front"):
        if not deque:
            print(-1)
        else:
            N = deque.popleft()
            print(N)
    elif(command[0] == "pop_back"):
        if not deque:
            print(-1)
        else:
            N = deque.pop()
            print(N)
    elif(command[0] == "size"):
        print(len(deque))
    elif(command[0] == "empty"):
        if not deque:
            print(1)
        else:
            print(0)
    elif(command[0] == "front"):
        if not deque:
            print(-1)
        else:
            N = deque.popleft()
            print(N)
            deque.appendleft(N)
    elif(command[0] == "back"):
        if not deque:
            print(-1)
        else:
            N = deque.pop()
            print(N)
            deque.append(N)
        