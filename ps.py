'''
[BOJ] 2577. 숫자의 개수
T: 1s
M: 128MB
'''
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)

count_numbers = [0 for _ in range(10)]

for i in range(len(result)):
    count_numbers[int(result[i])] += 1

for i in range(10):
    print(count_numbers[i])
