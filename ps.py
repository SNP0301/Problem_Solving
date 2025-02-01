"""
[복잡도] O(N)
    - 식의 길이 전체가 50 이하
[구상]
    - 최소값으로 만든다 -> 첫 "-" 연산자를 만나면 누적을 시작(괄호를 열고), "+" 연산자를 만나도 누적
        - 이후 2번째 "-"를 만나는 경우 누적+cur만큼 ans에서 뺴기 (괄호를 닫았기 때문)
    - 숫자가 0으로 시작할 수도 있으므로, 문자열 처리 점검 필요
    - **가장 처음과 마지막 문자는 숫자이다** --> "-"로 시작하는 경우의 수 고려할 필요 없음

"""
def make_number(l):
    num = 0
    for x in range(len(l)):
        num *= 10
        num += int(l[x])
    l = list()
    return num

cmd = input() ## 연산자 수 < 숫자 수 확인 필요
operator = list()
operand = list()
making_number = list()
num = 0
for i in range(len(cmd)):
    if cmd[i] == "+" or cmd[i] == "-":
        operator.append(cmd[i])
        if making_number:
            operand.append(make_number(making_number))
            making_number = list()

    else:
        making_number.append(cmd[i])

operand.append(make_number(making_number)) ## P1. if making_number로 점검 해야하나?

answer = operand[0]
accum = 0
is_subtracting = False
for i in range(len(operator)): ## operator[0] = "-", operator[1] = "+"
    if operator[i] == "-" and not is_subtracting: ## 빼기 시작 (괄호 열기)
        answer -= operand[i+1]
        is_subtracting = True
    elif operator[i] == "-" and is_subtracting: ## 빼기 끝, (괄호 닫기)
        answer -= operand[i+1]
    elif operator[i] == "+" and not is_subtracting:
        answer += operand[i+1]
        is_subtracting = False
    elif operator[i] == "+" and is_subtracting:
        answer -= operand[i+1]

print(answer)