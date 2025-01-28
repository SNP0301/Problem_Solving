"""
?
"""
import sys
input = sys.stdin.readline
sites = dict()

N, M = map(int,input().split())
for _ in range(N):
    info = list(input().split())
    sites[info[0]] = info[1] ## sites[사이트명] = 비밀번호
for i in range(M):
    info = input().rstrip()
    print(sites[info])