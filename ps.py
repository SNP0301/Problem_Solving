"""
[복잡도] O(n)
"""

N = int(input())
numbers = [0]+ list(map(int,input().split()))
bal_value = 0
cur = 1

for i in range(N): ## 풍선 순서는 자연수를 기준으로 하므로 array index에 맞추기 위해 -1
    bal_value = numbers[cur]
    numbers[cur] = 0
    print(cur,end=" ")
    if bal_value > 0:
        cnt = bal_value
        while cnt > 0:
            #print(bal_value,cnt)
            cur += 1
            if cur > N:
                cur = 0
            if numbers[cur] == 0:
                cnt += 1
            cnt -= 1
            if sum(numbers) == 0:
                break
    elif bal_value < 0:
        cnt = bal_value*-1
        while cnt > 0:
            #print(bal_value,cnt)
            cur -= 1
            if cur < 0:
                cur = N
            if numbers[cur] == 0:
                cnt += 1
            cnt -= 1
            if sum(numbers) == 0:
                break