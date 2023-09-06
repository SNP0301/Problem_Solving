import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = list()

for i in range(n):
    line = list(input().rstrip())
    graph.append([int(x) for x in line])

