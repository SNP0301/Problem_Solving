'''
[BOJ] 2669. 직사각형 네개의 합집합의 면적 구하기
T: 1초
M: 128MB
'''
import sys
input = sys.stdin.readline

board = [[0 for _ in range(100)] for _ in range(100)]
answer = 0

for _ in range(4):
    points = list(map(int, input().split()))
    x_one = points[0]
    y_one = points[1]
    x_two = points[2]
    y_two = points[3]

    for i in range(x_one,x_two,1):
        for j in range(y_one,y_two,1):
            if board[i][j] == 0:
                board[i][j] = 1
                answer += 1

print(answer)



