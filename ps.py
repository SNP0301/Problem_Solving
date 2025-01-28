N = int(input())
waiting = sorted(list(map(int,input().split())))
answer = 0

for i in range(len(waiting)):
    answer += waiting[i]*(N-i)

print(answer)
