"""

"""

N, K = map(int,input().split())
answer = list()
arr_idx = K-1 #2
arr = [i+1 for i in range(N)]


while arr:
    answer.append(arr[arr_idx])
    arr.remove(arr[arr_idx]) #pop?
    if arr_idx + K - 1 < len(arr):
        arr_idx += K - 1
    elif arr_idx + K - 1 >= len(arr) and len(arr) >= 1: ## 앞의 remove에서 숫자 만족하지 않는 경우 break
        arr_idx = (arr_idx + K - 1 ) % len(arr)
    if not arr:
        break

##print(answer)

print("<",end="")
for i in range(len(answer)):
    if i  != len(answer)-1:
        print("%d, "%(answer[i]),end="")
    else:
        print(answer[i],end=">")