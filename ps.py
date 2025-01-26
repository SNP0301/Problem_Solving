mandarat = list() ## 만다라트
for _ in range(9):
    mandarat.append(list(input().split()))

middle_goals = list() ## 중간 목표
for x in [1,4,7]:
    for y in [1,4,7]:
        middle_goals.append([mandarat[x][y],x,y])
middle_goals = sorted(middle_goals[:4]+middle_goals[5:])

dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

sub_goals = list()
for mg in range(8):
    sub_goals.append([]) ## 2차원
    x = middle_goals[mg][1]
    y = middle_goals[mg][2]
    for e in range(8): ## e of eight
        nx = x + dx[e]
        ny = y + dy[e]
        sub_goals[mg].append(mandarat[nx][ny])
    sub_goals[mg] = sorted(sub_goals[mg])
    ##for e in range(8): ## e of eight


for m in range(8):
    print("#%d. %s"%(m+1,middle_goals[m][0]))
    for s in range(8):
        print("#%d-%d. %s"%(m+1,s+1,sub_goals[m][s]))

    