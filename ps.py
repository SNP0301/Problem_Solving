import sys
input = sys.stdin.readline

n = input()
m = int(input())

n_size = len(n)-1
n = int(n)
ans = 0

button = [True]*10

mal = [int(x) for x in input().split()]

button[i] = False for i in mal

