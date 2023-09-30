'''
[BOJ] 1620. 나는야 포켓몬 마스터 이다솜
T: 1초
M: 256MB
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poketmon = ['empty']
poketmon_set = set()

for _ in range(n):
    p = input().strip()
    poketmon.append(p)
    poketmon_set.add(p)

#print(poketmon_set)
#print(poketmon)
for _ in range(m):
    quiz_poketmon = input().rstrip()
    if quiz_poketmon in poketmon_set:
        print(poketmon.index(quiz_poketmon))
    else:
        print(poketmon[int(quiz_poketmon)])