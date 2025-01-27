"""
*최빈 값이 여러개 있을 때에는 최빈값 중 두번째로 작은 값을 출력한다.
"""


N = int(input())
numbers = dict()
median_list = list()
mode_list = list()
exist_numbers = set()
num = 0
accum = 0
mode_cnt = -1

for i in range(N):
    num = int(input())
    if num in numbers:
        numbers[num] += 1
    else:
        numbers[num] = 1
    accum += num
    exist_numbers.add(num)
    mode_cnt = max(mode_cnt, numbers[num])
    median_list.append(num)

median_list = sorted(median_list)
##print(exist_numbers)

for i in exist_numbers:
    if numbers[i] == mode_cnt:
        mode_list.append(i)

mode_list = sorted(mode_list)


print(round(accum/N))
print(median_list[N//2])
if len(mode_list) == 1:
    print(mode_list[0])
else:
    print(mode_list[1])
print(max(list(exist_numbers))-min(list(exist_numbers)))
