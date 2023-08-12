import sys, heapq
input = sys.stdin.readline
plusHeap = []
minusHeap = []

for i in range(int(input())):
    n = int(input())
    if(n==0):
        if(not(plusHeap) and not(minusHeap)):
            print(0)
        else:
            if(plusHeap and not(minusHeap)):
                print(heapq.heappop(plusHeap))
            elif (not(plusHeap) and minusHeap):
                print(heapq.heappop(minusHeap)*-1)
            elif minusHeap and plusHeap and minusHeap[0] <= plusHeap[0]:
                print(heapq.heappop(minusHeap)*-1)
            else:
                print(heapq.heappop(plusHeap))
    else: ## push
        if(n<0):
            heapq.heappush(minusHeap, n*-1)
        else:
            heapq.heappush(plusHeap, n)
