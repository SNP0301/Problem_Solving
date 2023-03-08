word = input()
cnt = 0

for i in range(len(word)):
    if(ord(word[i])<=67):
        cnt += 3
    elif(ord(word[i])<=70):
        cnt += 4
    elif(ord(word[i])<=73):
        cnt += 5
    elif(ord(word[i])<=76):
        cnt += 6
    elif(ord(word[i])<=79):
        cnt += 7
    elif(ord(word[i])<=83):
        cnt += 8
    elif(ord(word[i])<=86):
        cnt += 9
    elif(ord(word[i])<=90):
        cnt += 10

print(cnt)