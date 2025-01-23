"""
* 주제가 가려져 있어도 2차원 문제인 척하는 1차원 문제 구분할 것

[배운 것]

[제약사항]
1. 가로 길이는 항상 100으로 고정
2. 모든 위치에서 상자의 높이는 1 이상 100 이하
3. 덤프 횟수는 1 이상 1000 이하
4. 평탄화가 완료되면 덤프를 수행할 수 없으므로 그 때 최고점과 최저점의 차를 반환
    - 평탄화 완료 여부는 max(arr)-min(arr) <= 1 으로 검증
5. 테스트 케이스가 10개로 고정
"""

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    answer = 0
    dump_limit = int(input())
    boxes = list(map(int,input().split()))

    while dump_limit > 0 :
        if max(boxes) - min(boxes) <= 1 :
            answer = max(boxes) - min(boxes)
            break
        elif max(boxes) - min(boxes) > 1:
            A = boxes.index(max(boxes))
            B = boxes.index(min(boxes))
            boxes[A] -= 1
            boxes[B] += 1
            dump_limit -= 1
            answer = max(boxes) - min(boxes)
        else:
            print("why")
            break

    print("#%d %d"%(test_case, answer))
    # ///////////////////////////////////////////////////////////////////////////////////