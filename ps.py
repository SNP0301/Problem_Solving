'''
[BOJ] 18258. 큐 2
T: 1 s
M: 512 MB
'''

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    command = list(input().split())
    if len(command) == 2:
        x = command[1]
    if command[0] == 'push':
        q.append(x)
    elif command[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q[0])
            q.popleft()
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif command[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
