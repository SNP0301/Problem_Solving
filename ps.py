"""
* 답이 여러개라면 그 중 땅의 높이가 가장 높은 것
** 땅의 높이는 256을 초과할 수 없다.
[구상]
- 채우기만하거나, 지우기만하거나, 채우면서 지우거나
    - 채우기만: 각 자리에서 Max까지 필요한 칸 수 *1만큼의 시간 소요
        - 단, 인벤토리 확인 필요
    - 지우기만:각 자리에서 min까지 지워야 하는 칸 수 *2만큼의 시간 소요
    - 채우면서 지우기: 
- 가능하기만 하면, [시간, 높이]로 answer에 추가
    - 정답으로는 시간 기준 오름차순, 높이 기준 내림차순으로 정렬해 [0]을 출력
"""
N, M, B = map(int,input().split())

land = list()
answer = list()
for _ in range(N):
    land.append(list(map(int, input().split())))

land_max = -1
land_min = 257
for i in range(N):
    land_max = max(land_max,max(land[i]))
    land_min = min(land_min,min(land[i]))
if land_min == land_max:
    answer.append([0,land_min])


##채우기만
current_time = 0
current_height = 0
is_stackable = True
B_tmp = B
for x in range(N):
    for y in range(M):
        B_tmp -= land_max-land[x][y]
        if B_tmp < 0:
            is_stackable = False
        else:
            current_time += land_max-land[x][y]

if is_stackable:
    ##print("stack",current_time,current_height)
    answer.append([current_time, land_max])

##지우기만
current_time = 0
current_height = 0
for x in range(N):
    for y in range(M):
        current_time += (land[x][y]-land_min)*2
##print("erase",current_time,current_height)
answer.append([current_time,land_min])


## 쌓고 지우기
current_time = 0
current_height = 0
for target in range(land_min+1,land_max+1,1): ##(land_max-land_min-c)만큼 쌓고, c만큼 지우기
    B_tmp = B
    used_block = 0
    acq_block = 0
    is_stackable = True
    for x in range(N):
        for y in range(M):
            if land[x][y] < target:
                used_block += target-land[x][y]
                current_time += target-land[x][y]
                ##print("at [%d][%d], current_time is %d"%(x,y,current_time))
                if B_tmp < 0:
                    is_stackable = False

            elif land[x][y] > target:
                ##print("at [%d][%d], current_time is %d"%(x,y,current_time))
                current_time += (land[x][y]-target)*2
                acq_block += land[x][y]-target
                ##print("at [%d][%d], current_time is %d"%(x,y,current_time))
    if B_tmp + acq_block >= used_block:
        ##print("total",c,current_time,current_height)
        answer.append([current_time,target])
    current_time = 0
    current_height = 0



################################
answer = sorted(answer, key= lambda k: (k[0],-k[1]))
#print(answer)
print(answer[0][0],answer[0][1])