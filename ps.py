"""
* M이상 N이하, 소수가 하나 이상 있는 입력만
** 한 줄에 하나씩, 증가하는 순서대로 소수 출력

[구상]
    - 1~N 사이에 존재하는 소수 x를 미리 구해 is_prime[x]에 'True' 로 저장
"""

M, N = map(int,input().split())
is_prime = [True for _ in range(N+1)]
is_prime[1] = False

for i in range(2, N):
    if is_prime[i]:
        n = i*2
        while n <= N:
            is_prime[n] = False
            n += i

for i in range(M,N+1):
    if is_prime[i]:
        print(i)