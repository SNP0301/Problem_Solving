"""
* 반복문,조건문의 역할을 mece하게 이해했다면 안 틀렸을 것,,,
** 손구현 먼저 하자.
"""
def BFS(x,N):
    queue = [x]
    while queue:
        x = queue.pop()
        for j in range(1,N+1):
            if arr[x][j] == 1:
                ##print("from %d to %d"%(x,j))
                queue.append(j)
                answer_set.add(j)
                arr[x][j] = -1

computers = int(input())

if computers == 1:
    print(0)
else:
    num = int(input())
    arr = [[0 for _ in range(computers+1)] for _ in range(computers+1)]
    answer = 0
    answer_set = set()

    for _ in range(num):
        start,end = map(int,input().split())
        
        if start > end:
            start,end = end,start
        arr[start][end] = 1
        arr[end][start] = 1

    for i in range(2,computers+1):
        if arr[1][i] == 1:
            BFS(1,computers)
    

    if 1 in answer_set:
        print(len(answer_set)-1)
    else:
        print(len(answer_set))

