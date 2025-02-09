"""
[복잡도] O(NlgN)
    - 너비는 N, 깊이는 M이 결정?

[구상]
    I: 자연수 1<=M<=N<=8
    O: 조건을 만족하는 수열을 중복 없이 출력
        - 수열은 사전 순으로 증가하는 순서로 출력
            * 탐색 자체를 range(1,N+1)내에서 수행하므로 사전 순으로 탐색

[테스트 케이스]

"""
N, M = map(int,input().split())

arr = list()

def search(): ### 종료 조건 => 단위 작업 => 재귀 호출
    if len(arr) == M:       ## 1) 종료조건: 수열의 길이인 M개를 다 채웠으면 종료
        for i in arr:
            print(i,end=" ")
        print()
        return
    else:
        for i in range(1,N+1):
            if i not in arr:
                arr.append(i)       ## 2-1) 단위 작업: 중복되지 않는 요소를 넣고
                search()            ## 3) 재귀 호출
                arr.pop()           ## 2-2) 단위 작업: 3)에서 탐색이 끝났으면 다시 돌아오자마자 넣었던 요소 빼주기

search()