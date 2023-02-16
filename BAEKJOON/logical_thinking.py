avg = 0
n = int(input())

score = list(map(float,input().split()))

M = max(score)

for i in range(n):
    score[i] = score[i]/M*100

for i in range(n):
    avg += score[i]

print(avg/n)