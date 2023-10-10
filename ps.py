'''
[BOJ] 9184. 신나는 함수 실행
T: 1s
M: 128MB
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def recur(a,b,c):
    if a*b*c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        print(a,b,c)
        print(type(a),type(b),type(c))
        return recur(20,20,20)
    elif a<b and b<c:
        return recur(a,b,c-1)+recur(a,b-1,c-1)-recur(a,b-1,c)

    return recur(a-1,b,c) + recur(a-1,b-1,c)+recur(a-1,b,c-1)-recur(a-1,b-1,c-1)

while True:
    a,b,c = map(int,input().split())
    if a== -1 and b==-1 and c==-1:
        break
    else:
        print("w(%d, %d, %d) = %d"%(a,b,c,recur(a,b,c)))

