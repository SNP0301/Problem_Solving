"""
* 숫자 카드의 범위가 -10000000~10000000이므로, 리스트로는 불가능
"""

N = int(input())
sg_dct = dict()
numbers = input().split()
#print(numbers)
for i in range(N):
    if numbers[i] in sg_dct:
        sg_dct[numbers[i]] += 1
    else:
        sg_dct[numbers[i]] = 1

#print(sg_dct)
M = int(input())
check_numbers = input().split()
for i in range(M):
    if check_numbers[i] in sg_dct:
        print(sg_dct[check_numbers[i]],end=" ")
    else:
        print(0,end=" ")