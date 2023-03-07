A,B = map(int,input().split())

def sangsu(givenNum):
    sangsuNum = 0
    sangsuNum += (givenNum%10)*100
    sangsuNum += (givenNum//100)
    givenNum %= 100
    sangsuNum += (givenNum//10)*10
    return sangsuNum

print(max(sangsu(A),sangsu(B)))