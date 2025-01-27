"""
*최빈 값이 여러개 있을 때에는 최빈값 중 두번째로 작은 값을 출력한다.
"""


N = int(input())
numbers = [[i,0] for i in range(-4000,4001,1)]
exist_numbers = list()
accum = 0
mode_cnt = -1

for i in range(N):
    num = int(input())
    numbers[num+4000][1] += 1
    accum += num
    print(numbers[num+4000])

for i in range(8001):
    if numbers[i][1] ^ 0:
        exist_numbers.append(numbers[i])

exist_numbers = sorted(exist_numbers, key = lambda x: -x[1])


print(round(accum/N))
print(exist_numbers[len(exist_numbers)//2][0])
if exist_numbers[0][1] == exist_numbers[1][1]:
    print(exist_numbers[1][0])
else:
    print(exist_numbers[0][0])

