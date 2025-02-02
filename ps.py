"""
[복잡도] O(N)
    - left 포인터와 right 포인터가 각각 N번 이동하므로 O(n)
        - right 포인터가 한번 움직일 때, 최악의 경우 left 포인터가 N-1회 움직이는 경우 N*(N-1)로 생각할 수 있으나, 이런 케이스는 최대 1번 발생

*무조건 다시 풀어볼 것.
"""
N = int(input())
thr = list(map(int,input().split()))
thr_dct = dict()
fruit_type_counter = 0
answer = 0
lft = 0
rgt = 0

for rgt in range(N):
    if thr[rgt] in thr_dct:
        thr_dct[thr[rgt]] += 1
    elif thr[rgt] not in thr_dct:
        thr_dct[thr[rgt]] = 1
        fruit_type_counter += 1
    
    while fruit_type_counter > 2:
        thr_dct[thr[lft]] -= 1
        if thr_dct[thr[lft]] == 0:
            del thr_dct[thr[lft]]
            fruit_type_counter -= 1
        lft += 1

    answer = max(answer,rgt-lft+1)

print(answer)