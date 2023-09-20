'''
[BOJ] 2529. 부등호
T: 1초
M: 256MB
'''
import sys
input = sys.stdin.readline

n = int(input())
sign = input().split()
numbers = [i for i in range(0,10)]
print(numbers[1:])


def recur(idx:int,numbers:list,answer:int): ## 숫자의 idx번째를 채워야하는데, 재료는 numbers가 있다. 부등호에 맞는 숫자(x)가 있으면 answer = answer*10+x로 recur해라
    if idx == n:
        print(answer)
    possible = False
    if sign[idx-1] == ">":
        for x in numbers:
            if answer%10 > x:
                next_numbers = numbers.remove(x)
                recur(idx+1,next_numbers,answer*10+x)
                possible = True
    elif sign[idx-1] == "<": ## sign=="<"
        for x in numbers:
            if answer%10 < x:
                next_numbers = numbers.remove(x)
                recur(idx+1,next_numbers,answer*10+x)
                possible = True
    if not possible:
        return

for i in range(1,10):
    first_numbers = numbers.remove(i)
    recur(1,first_numbers,i)