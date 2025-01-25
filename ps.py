"""
[구상]
- 10000 개의 element가 있는 arr에 미리 값을 계산해두기
- 시간 복잡도: 이전 arr[x]에 사용했던 값을 int 하나로 기억해두면 N**2은 피할 것으로 예상 (확인 필요)

"""

def get_digits(i):
    denom = 10
    digit = 1
    while True:
        if i // denom == 0:
            return digit
        else:
            denom *= 10
            digit += 1

    


N = int(input())

arr = [0 for i in range(N+2)] ## i번째 값에 i번째 영화 제목에 들어간 수를 저장하는 배열
arr[1] = 666
arr[2] = 1666
calculated = 1667

for i in range(3, len(arr)):
    found = False
    while not found:
        num = calculated
        str_num = str(num)
        for j in range(get_digits(num)-2,-1,-1):
            if int(str_num[j:j+3]) == 666:
                arr[i] = num
                calculated = num + 1
                found = True
                break
        if not found:
            calculated += 1

        
        
        



print(arr[N])

