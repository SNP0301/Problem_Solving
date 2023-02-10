A, B = map(int,input().split())
C = int(input())

total = (A*60)+B+C

H = (total//60)%24
M = total%60

print(H, M)