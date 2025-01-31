"""
[복잡도] 계단 갯수 최대 300개이며 연산도 각 계단에 대해 1번씩인데, index 참조

* 2+1, +2 말고 1+2는 왜 고려하지 않지? 왜 최대 2칸, 3칸 단위로 나누는거지?
"""

N = int(input())

steps = [0]+[int(input()) for _ in range(N)]
answer= [0 for _ in range(301)]

if N == 1:
    answer[1] = steps[1]
elif N == 2:
    answer[2] = steps[1] + steps[2]
else :
    answer[1] = steps[1]
    answer[2] = steps[1] + steps[2]
    answer[3] = max(steps[1] + steps[3], steps[2]+steps[3]) ## 1+2로 왔거나, 2+1로 왔거나. (1+1+1)은 해당 x
    for i in range(4,N+1):
        answer[i] = max(answer[i-3]+steps[i-1]+steps[i], answer[i-2]+steps[i])
print(answer[N])