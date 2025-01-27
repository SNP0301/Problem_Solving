"""
* 중요도가 같은 문서가 여러 개 있을 수도 있다.

[복잡도]
    - 우선순위가 역순으로 주어져도 100*100
"""

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    tmp_paper = list(map(int,input().split()))
    paper = list()
    priority = list()
    cnt = 0
    for i in range(len(tmp_paper)):
        paper.append([i,tmp_paper[i]])
        priority.append(tmp_paper[i])
    #print(paper)
    priority = sorted(priority)
    #print(priority)
    while True:
        is_printable = True
        if max(priority) > paper[0][1]:
            is_printable = False
            paper = paper[1:]+paper[0]
        
        if is_printable:
            if paper[0][0] == M:
                print(cnt)
            else:
                priority.pop(len(priority)-1)
                paper = paper[1:]
                print(paper)
                cnt += 1


            