"""

[구상]
- 10,000길이의 dict 선언
- 숫자가 등장하면 dict[해당 숫자] = 1
- for(1,10001)에서 if dict[해당 숫자] = 1 이면 해당 숫자 출력
"""

N = int(input())
numbers = [0 for _ in range(10002)]

for i in range(N):
    n = int(input())
    numbers[n] += 1
    ##print(n)

print()
for i in range(1, 10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)
