"""
[복잡도] O(log n)
    - heapq는 push, pop 모두 O(log n)을 따른다
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())
hpq = list()
heapq.heapify(hpq)

for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        if not hpq:
            print(0)
        elif hpq:
            print(heapq.heappop(hpq)*-1)
    else:
        heapq.heappush(hpq,cmd*-1)
