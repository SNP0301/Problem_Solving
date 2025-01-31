"""
[복잡도] O(n)
- 괄호 문자 최대 100,000개
    - 전체 괄호에 대해 순차적으로 한번씩 접근하고, 접근할 때 최대 2개의 요소에 접근
"""

bar = input()
stk = []
answer = 0
cnt = 0
for i in range(len(bar)):
    if bar[i] == '(' and bar[i+1] == '(':
        cnt += 1
    elif bar[i] == ')':
        if bar[i-1] == '(':
            answer += cnt
        else:
            cnt -= 1
            answer += 1
    #print(i,bar[i],answer)


print(answer)