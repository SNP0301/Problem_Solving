"""
[배운 것]
- round의 인자로 들어가는 수의 소수점 자릿수가 커지면 오차가 발생할 수 있다.
- my_round로 대체해야 한다는 아이디어는 떠올리지 못했다
    - 강사님 말씀대로, 함수/메서드가 어떻게 동작하는지 정확하게 알고 사용할 것.
"""

def my_round(i):
    if i - int(i) >= 0.5:
        return int(i) + 1
    else: return int(i)

n = int(input())
score_list = list()
cut = 0
answer = 0

for _ in range(n):
    score_list.append(int(input()))

if n == 0:
    print(0)
elif 1<= n <= 3:
    print(my_round(sum(score_list)/len(score_list)))
elif n > 3:
    score_list = sorted(score_list)
    cut = my_round(n * 0.15)
    ##print(n,n*0.15,cut)
    score_list = score_list[cut:-cut]
    ##print(score_list)
    print(my_round(sum(score_list) / len(score_list)))