'''
[BOJ] 4949. 균형잡힌 세상
T: 1초
M: 128MB
'''
import sys
input = sys.stdin.readline

while True:
    p = input()
    if p == '.' or p == '.\n':
        break
    right = True
    ps_stack = list()

    for i in range(len(p)):
        if p[i] == '(':
            ps_stack.append('(')
        elif p[i] == '[':
            ps_stack.append('[')
        elif p[i] == ')':
            if not ps_stack:
                right = False
            elif ps_stack[-1] != '(':
                right = False
            else:
                ps_stack.pop()
        elif p[i] == ']':
            if not ps_stack:
                right = False
            elif ps_stack[-1] != '[':
                right = False
            else:
                ps_stack.pop()
    if right and not ps_stack:
        print("yes")
    else:
        print("no")