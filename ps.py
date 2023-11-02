'''
[BOJ] 2839. 설탕 배달
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

n = int(input())

for_five = n // 5
for_three = 0
available = []
possible = False

if n % 5 == 0:
    possible = True
    available.append(n//5)
if (n - ((n//5)*5))% 3 == 0:
    possible = True
    for_five = n//5
    for_three = (n-(n//5*5))//3
    available.append(for_five + for_three)
if n % 3== 0:
    possible = True
    available.append(n//3)

for_five = n // 5
for i in range(n//5):
    if (n-(for_five*5))%3 == 0:
        available.append(for_five + ((n-(for_five*5))//3))
        possible = True
    for_five -= 1

if possible:
    print(min(available))
else:
    print(-1)