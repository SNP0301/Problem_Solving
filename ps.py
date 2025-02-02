"""
[시간복잡도] O(N*M)

소요시간 총 20분 내외
    - 구상: ~15분
    - 구현: ~5분
"""
N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
M, K = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(M)]
C = [[0 for _ in range(K)] for _ in range(N)]

for x in range(N):
    for y in range(K):
        for m in range(M):
            C[x][y] += A[x][m] * B[m][y]

for c in C:
    for e in c:
        print(e,end=" ")
    print()