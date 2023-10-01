'''
[BOJ] 18870. 좌표 압축
T: 2초
M: 512MB
'''
import sys
input = sys.stdin.readline

x = input()
cnt = 0

for i in range(len(x)):
    print(x[i],end="")
    cnt += 1
    if cnt == 10:
        print("\n",end="")
        cnt = 0