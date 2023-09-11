'''
[BOJ] 11052. 카드 구매하기
T: 1초
M: 256MB
'''
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
whole_price = list(map(int,input().split()))
per_price = [[0,0] for _ in range(n)]
answer = 0

##print(whole_price)

for i in range(n):
    per_price[i][0] = i+1
    per_price[i][1] = whole_price[i]/(i+1)



per_price.sort(key=lambda x: (x[1],x[0]),reverse=True)

per_price = deque(per_price)

##print(per_price)


remain = n

while remain:
    number_of_set = remain//per_price[0][0]
    if number_of_set >= 1:
        ##print("How many set?: [%d]"%(number_of_set))
        answer += (number_of_set)*per_price[0][1]*per_price[0][0]
        remain = remain%per_price[0][0]
    else:
        per_price.popleft()

print(int(answer))