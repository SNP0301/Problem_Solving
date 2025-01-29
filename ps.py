"""
* 리스트 슬라이스 연습용 문제

[배운 것]
- 조건문 분기를 최대한 꼼꼼하게 해야 구현도 쉽다
- idx 0, 1인 경우를 따로 세면 나중에 불편해진다.
"""

P = int(input())
for p in range(1,P+1):
    answer = 0
    info = list(map(int,input().split()))
    info.pop(0)
    stood = [info.pop(0)]
    for _ in range(19):
        cur = info.pop(0)
        #print(cur,stood)
        if cur > stood[-1]: ##최대값보다 크다면
            stood.append(cur)
        elif cur < stood[0]: ##최소값보다 작다면
            #print("%d made +%d"%(cur,len(stood)))
            answer += len(stood)
            stood = [cur] + stood
        elif stood[0]<cur<stood[-1]: ##그 사이라면
            for i in range(len(stood)-1,-1,-1):
                if cur > stood[i]: ## 자리를 찾으면
                    ##print("%d made +%d"%(cur,len(stood[i:])))
                    answer += len(stood[i:])-1
                    #print(stood[:i+1])
                    #print(stood[i+1:])
                    new_stood = stood[:i+1] + [cur] + stood[i+1:]
                    stood = new_stood
                    break
                
    ##print(info)
    #print(stood)
    print(p, answer)
