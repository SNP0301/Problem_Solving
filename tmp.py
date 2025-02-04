T = int(input())
for tc in range(1, T + 1):
    # N : 화덕 크기, M : 피자 개수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    temp = [0] * (M + 1)
    for i in range(M):
        temp[i + 1] = arr[i]

    pizza = []
    for idx, c in enumerate(temp):  # idx : 피자번호, c : 치즈양
        pizza.append([idx, c])  # [[0, 0], [1, 7], [2, 2], [3, 6], [4, 5], [5, 3]]
    pizza = pizza[1:]  # [[1, 7], [2, 2], [3, 6], [4, 5], [5, 3]]

    # 빈 화덕에 피자 넣기
    bake = []
    for _ in range(N):
        p = pizza.pop(0)
        bake.append(p)

    # print(bake)     # [[1, 7], [2, 2], [3, 6]] >> 화덕에 있는 피자
    # print(pizza)    # [[4, 5], [5, 3]] >> 대기중인 피자

    # 피자개수 1개 남을때 까지 반복
    while len(bake) > 1:
        p = bake.pop(0)  # 피자 꺼내서
        c = p[1] // 2  # 피자 치즈 양 확인

        if c != 0:  # 0이 아니면
            p[1] = c
            bake.append(p)  # 다시 넣기

        else:  # 0이고
            if pizza:  # 굽히지 않은 피자가 있다면
                new_p = pizza.pop(0)  # 새로운 피자 넣기
                bake.append(new_p)

    print(f'#{tc} {bake[0][0]}')