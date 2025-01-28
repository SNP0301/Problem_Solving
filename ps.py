"""
[구상]
- set으로 중요도 검증, [초기 순서, 중요도]
"""

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    papers = list(map(int,input().split()))
    priority_dct = dict()
    printer = list()
    for i in range(N):
        if papers[i] not in priority_dct:
            priority_dct[papers[i]] = 1
        else:
            priority_dct[papers[i]] += 1
        printer.append([i,papers[i]])
    not_printed = True
    cnt = 1
    ##print(len(printer))
    #print(priority_dct)
    if len(printer) == 1:
        print(1)
        not_printed = False

    while not_printed :
        if len(printer) == 1:
            print(cnt)
            break
        elif len(printer) >= 2:
            if printer[0][1] < max(priority_dct):
                printer = printer[1:] + [printer[0]]
                ##print("moved" + str(printer))
            elif printer[0][1] == max(priority_dct):
                if printer[0][0] == M:
                    print(cnt)
                    not_printed = False
                elif printer[0][0] != M:
                    cnt += 1
                    priority_dct[printer[0][1]] -= 1
                    if priority_dct[printer[0][1]] == 0:
                        priority_dct.pop(printer[0][1])
                    printer = printer[1:]

            




