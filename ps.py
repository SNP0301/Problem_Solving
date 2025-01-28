"""

"""

N = int(input())
given_lst = list()
chk_lst = [i for i in range(N,0,-1)]
given_dct = dict()

tmp_stk = list()
my_stk = list()

answer_lst = list()

is_stackable = True
cur = N

for i in range(1,N+1):
    n = int(input())
    given_lst.append(n) # 4 3 6 8 7 5 2 1
    given_dct[n] = i ## given_dct[숫자]=위치

while len(my_stk) < N:
    if given_dct[cur] != 0:
        mov = given_lst.pop()
        tmp_stk.append(mov)
        answer_lst.append("-")
        given_dct[mov]=0
    else:
        mov = tmp_stk.pop()
        my_stk.append(mov)
        answer_lst.append("+")
        cur -= 1

if my_stk == chk_lst:
    for i in range(len(answer_lst)-1,-1,-1):
        print(answer_lst[i])
else:
    print("NO")
