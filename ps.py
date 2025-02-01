"""
[복잡도] O(N**2) 
    - 자료구조가 100,000개, 삽입할 수열의 길이가 100,000인 경우  10**10승 수행?
        - 다른 방법이 필요하다.
[구상]
    - 단순하게 연산 및 탐색을 하면 무조건 시간 초과가 나올 것으로 예상
        - 규칙, 줄일 수 있는 방법 찾기
        - 결론: queuestack 및 입력값의 특성상 stack들은 출력에 영향을 미치지 않는다.
    - stack은 제외하고, queue끼리만 합쳐 하나의 queue를 만들고 이름은 queuestack으로 선언
        - 초기의 queuestack에는 queuestack을 이루고 있는 queue의 수만큼만 원소가 존재
        - 수열 C로 주어지는 입력값 또한 queuestack에 push
        - 수열 C의 길이(M)만큼 popleft 한 것이 전체 queuestack의 결과
    - **시간복잡도 및 입력의 크기를 고려해 import sys 사용**

"""
import sys
input = sys.stdin.readline
from collections import deque

queuestack = deque()
N = int(input())
series_ds = list(map(int,input().split())) ## series of data structure
ds_value = list(map(int,input().split()))
M = int(input())
C = map(int,input().split())

for i in range(N-1,-1,-1):
    if series_ds[i] == 0:
        queuestack.append(ds_value[i])
for c in C:
    queuestack.append(c)

for i in range(M):
    print(queuestack.popleft(),end=" ")