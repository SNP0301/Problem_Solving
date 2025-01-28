"""
set.union()으로는 못 푸나?
    - 컴퓨터 1대당 각 1개씩, 총 100개의 set을 만들고, 해당 컴퓨터와 연결된 node 번호를 set.add()
    - answer_set = answer_set.union(~~)
"""
T = int(input())

answer_list = [0 for _ in range(11)]
answer_list[1] = 1
answer_list[2] = 2
answer_list[3] = 4
for i in range(4,11):
    answer_list[i] = answer_list[i-1] + answer_list[i-2] + answer_list[i-3]

for _ in range(T):
    n = int(input())
    print(answer_list[n])