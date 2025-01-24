"""
* 카드가 1장 남을 때까지
** 1<= N <= 500,000
"""

N = int(input())
cnt = 1
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    while True:
        if 2**cnt<N<=2**(cnt+1):
            print(2**(cnt+1)-(2**(cnt+1)-N)*2)
            break
        else:
            cnt += 1