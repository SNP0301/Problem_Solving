word = input()
arr = []

for i in range(26):
    arr.append(0)

for i in range(len(word)):
    if(ord(word[i])>=97):
        arr[ord(word[i])-97] += 1
    elif(ord(word[i])>=65):
        arr[ord(word[i])-65] += 1

most = max(arr)
check = 0
idx = 0

for i in range(26):
    if(arr[i]==most):
        check += 1
        idx = i

if (check>=2):
    print("?")
else:
    print(chr(idx+65))

        
