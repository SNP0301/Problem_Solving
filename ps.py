'''
[BOJ] 2953. 나는 요리사다
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

score = list()

for i in range(5):
    score.append(sum(list(map(int,input().split()))))


print(score.index(max(score))+1, max(score))