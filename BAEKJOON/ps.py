t = int(input())

for i in range(t):
    r, s = map(str,input().split())
    for j in range(len(s)):
        for k in range(int(r)):
            print("%c"%(s[j]),end="")
    print()