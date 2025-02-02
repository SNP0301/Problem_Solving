"""
[복잡도] O(n)
    - 화학식의 길이가 10,000을 넘지 않는다.

[실수]
    - 분기를 너무 자세하게 나눠서, mece하지 않았다.
    - 간단하게 생각할 필요가 있다 (겹치는 부분 합치기 등)
"""


formula = input()
chem_dct = dict()
chem_dct["H"] = 1
chem_dct["C"] = 12
chem_dct["O"] = 16
stk = []

for x in formula:
    if x in chem_dct:
        stk.append(chem_dct[x])
    elif x == "(":
        stk.append(x)
    elif x == ")":
        tmp_answer = 0
        while True:
            cur = stk.pop()
            if cur == "(":
                break
            tmp_answer += cur
        if tmp_answer == 0:
            continue
        else:
            stk.append(tmp_answer)
    else:
        n = stk.pop()
        tmp_answer = n*int(x)
        stk.append(tmp_answer)

print(sum(stk))
