n, m = map(int, input().split())
lst = [i for i in range(1,n+1)]
for _ in range(m):
    i, j, k= map(int, input().split())
    lst = lst[:i-1]+ lst[k-1:j] + lst[i-1:k-1]+lst[j:]
print(lst)