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

for i in range(n):
    print(max(paper[i])*2)
    answer += (max(paper[i])*2)

print(answer)

for i in range(m):
    for j in range(n):## (i,j) = (0,0)(1,0)(2,0) / (0,1)(1,1)(2,1)
        column_max = max(column_max,paper[j][i])
        ##print(j,i) round check
    print("%d column max: %d"%(i,column_max))
    answer += (column_max*2)
    column_max = 1

print(answer)

print(answer)
