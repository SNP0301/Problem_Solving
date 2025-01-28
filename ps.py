"""
- 랜선 길이가 2**31-1로 주어지고, N이 1,000,000인 경우
    - 1부터 하나씩 잘라 올라가면 초과하나?
- 2**move_size로 탐색
"""

K, N = map(int,input().split())
cables = list()
for i in range(K):
    cables.append(int(input()))

#print(cables)
current_length = 1
move_size = 31
cnt = 0
answer = list()
current_N = 0
go_up = True
go_down = not go_up

while cnt <= 30:
    cnt += 1
    current_N = 0
    for k in range(K):
        current_N += cables[k]//current_length
    if current_N >= N:
        answer.append([current_N,current_length])
    if go_up:
        if current_N > N:
            move_size += 1
            current_length += move_size**2
            go_up = True
        elif current_N < N:
            move_size -= 1
            current_length -= move_size**2
            go_down = True
        elif current_N == N:
            move_size == 0
            current_length += move_size**2
    elif go_down:
        if current_N > N:
            move_size -= 1
            current_length += move_size**2
            go_down = False
        elif current_N < N:
            move_size += 1
            current_length -= move_size**2
            go_down = True
        elif current_N == N:
            move_size == 0
            current_length += move_size**2
    if current_N <= 0:
        move_size = 1
        current_length = 1

answer = sorted(answer,key = lambda x: (-x[1],x[0]))
print(answer[:10])
print(answer[0][1])