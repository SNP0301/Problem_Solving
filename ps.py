'''
[BOJ] 14889. 스타트와 링크

T: 2s
M: 512MB
'''
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
stat_max = -1
stat_min = 10001
start_stat = 0
link_stat = 0
stat = list()
entries = list()
member_list = [i for i in range(n)]

for _ in range(n):
    stat.append(list(map(int,input().split())))

for i in combinations(member_list, n//2):
    entries.append(list(i))

##print(len(entries)) ## nCn//2
#print(entries)

stat_diff = 99999
for e in entries:
    stat_min = 10001

    #print(e)
    start = e
    link = list()
    for m in member_list:
        if m not in e:
            link.append(m)

    for u in range(n):
        for v in range(n):
            if u in start and v in start:
                start_stat += stat[u][v]
            elif u in link and v in link:
                link_stat += stat[u][v]
    #print(start, start_stat)
    #print(link, link_stat)
    stat_diff = min(max(start_stat-link_stat, link_stat-start_stat),stat_diff)
    #print(stat_diff, stat_min,"\n")


    start_stat = 0
    link_stat = 0

print(stat_diff)