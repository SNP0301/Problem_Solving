'''
[BOJ] 2083. 럭비 클럽
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

while True:
    member = list(input().split())
    if member[0] == '#' and member[1] == '0' and member[2] == '0':
        exit()

    if int(member[1]) > 17 or int(member[2]) >= 80:
        print(member[0],"Senior")
    else:
        print(member[0],"Junior")