"""
set.union()으로는 못 푸나?
    - 컴퓨터 1대당 각 1개씩, 총 100개의 set을 만들고, 해당 컴퓨터와 연결된 node 번호를 set.add()
    - answer_set = answer_set.union(~~)
"""
computers = int(input())
num_of_edges = int(input())
answer_list = [ set() for _ in range(computers+1)]

if computers == 1:
    print(0)
else:
    for _ in range(num_of_edges):
        start, end = map(int,input().split())
        #print(start,end)
        answer_list[start].add(end)

    answer_set = answer_list[1]
    for i in range(1,computers+1):
        if i in answer_list[1]:
            answer_set = answer_set.union(answer_list[i])
            #print(i,answer_set)
    for i in range(computers,0,-1):
        if i in answer_list[1]:
            answer_set = answer_set.union(answer_list[i])
            #print(i,answer_set)

    if 1 in answer_set:
        print(len(answer_set)-1)
    else:
        print(len(answer_set))