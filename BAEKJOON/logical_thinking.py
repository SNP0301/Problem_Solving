n = int(input())

for i in range(n):
    accum = 0
    score = 0
    arr = input()
    for i in range(len(arr)):
        if(arr[i]=='O'):
            accum += 1
            score += accum
        else:
            accum = 0
    print(score)
