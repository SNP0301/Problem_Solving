'''
[BOJ] 9012. 괄호
T: 1초
M: 128MB
'''
import sys
input = sys.stdin.readline

ps_open = []

stack = [1,2,3]

t = int(input())

for _ in range(t):
    ps = input()
    ps_open = list()
    possible = True
    for i in range(len(ps)):
        if ps[i] == "(":
            ps_open.append("(")
        elif ps[i] == ")":
            if ps_open:
                current = ps_open[-1]
                if current == "(":
                    ps_open.pop()
                i += 1
            elif not ps_open:
                possible = False
                i += 1
                break

    
    if ps_open:
        possible = False
    
    if possible:
        print("YES")
    else:
        print("NO")

            
