'''
[BOJ] 2506. 점수 계산
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

n = int(input())

right_answer = list(map(int,input().split()))
current_score = 0
answer = 0
for i in range(n):
    if right_answer[i] == 1:
        current_score += 1
        answer += current_score
    elif right_answer[i] == 0:
        current_score = 0

print(answer)