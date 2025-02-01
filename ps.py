"""
[복잡도] O(n)?
    - 나무의 수 * 탐색 수
    - 나무 길이는 탐색 크기 설정할 때 말고는 별로 안 중요할 것 같은데 맞나?

* sum이랑 전체에 대해 조건문 한번, 계산 한번 거는 것 중 뭐가 더 오래 걸리나?
"""

def get_wood(cur_trees):
    wood = 0
    for i in cur_trees:
        if i >= 0:
            wood += i
    return wood

N, M = map(int,input().split())
trees = list(map(int,input().split()))
answer = list()

sz = 2000000000 ## 2 000 000 000

while sz != 1:
    cur_trees = [max(0,i-sz) for i in trees]
    if get_wood(cur_trees) >= M:
        answer.append(sz)
        #print(sz)
    sz = max(1,int(sz//2))

sz = 1

if answer:
    cur = max(answer)
else:
    cur = 0

while True:
    cur_trees = [max(0,i-sz-cur) for i in trees]
    if get_wood(cur_trees) >= M:
        answer.append(cur+sz)
        #print(cur+sz)
        sz *= 2
        cur += sz
    elif get_wood(cur_trees) < M:
        sz = max(1,int(sz//2))
        cur -= sz
    if sz == 1:
        while True:
            cur_trees = [max(0,i-sz-cur) for i in trees]
            if get_wood(cur_trees) >= M:
                answer.append(cur+sz)
                #print("#%d"%cur)
                cur += 1
            elif get_wood(cur_trees) < M:
                #print("%d is failed"%cur)
                break
        break

if answer:
    print(max(answer))
else:
    print(1)