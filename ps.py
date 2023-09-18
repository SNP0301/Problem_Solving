'''
[BOJ] 16931. 겉넓이 구하기
T: 1초
M: 512MB
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
paper = list()
answer = 2*n*m ## 위 + 아래
column_max = 0
print(answer)

for i in range(n):
    paper.append(list(map(int,input().split())))

