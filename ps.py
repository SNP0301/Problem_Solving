T = int(input())

for _ in range(T):
    n = int(input())
    fashion_dct = dict()
    answer = 1
    for _ in range(n):
        info = list(input().split())
        if info[1] in fashion_dct:
            fashion_dct[info[1]] += 1
        else:
            fashion_dct[info[1]] = 1
    for x in fashion_dct:
        answer *= fashion_dct[x]+1
    print(answer-1)