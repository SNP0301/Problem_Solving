'''
[BOJ] 28279. 덱 2
T: 2 s
M: 1024 MB
'''

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    command = list(map(int,input().split()))
    if (len(command) == 2):
        x = command[1]

    if command[0] == 1:
        d.append(x)
    elif command[0] == 2:
        d.appendleft(x)
    elif command[0] == 3:
        if not d:
            print(-1)
        else:
            a = d.pop()
            print(a)
    elif command[0] == 4:
        if not d:
            print(-1)
        else:
            a = d.popleft()
            print(a)
    elif command[0] == 5:
        print(len(d))
    elif command[0] == 6:
        if not d:
            print(1)
        else:
            print(0)
    elif command[0] == 7:
        if not d:
            print(-1)
        else:
            print(d[-1])
    elif command[0] == 8:
        if not d:
            print(-1)
        else:
            print(d[0])
        


