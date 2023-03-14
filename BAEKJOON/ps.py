word = input()
cnt = 0
word_cnt = 0

while True:
    if(cnt<len(word)):
        currentWord = word[cnt:cnt+2]
        if(currentWord=='c='):
            word_cnt += 1
            cnt += 2
        elif(currentWord=='c-'):
            word_cnt += 1
            cnt += 2
        elif((currentWord=='dz')and(word[cnt+2]=='=')):
            word_cnt += 1
            cnt += 3
        elif(currentWord=='d-'):
            word_cnt += 1
            cnt += 2
        elif(currentWord=='lj'):
            word_cnt += 1
            cnt += 2
        elif(currentWord=='nj'):
            word_cnt += 1
            cnt += 2
        elif(currentWord=='s='):
            word_cnt += 1
            cnt += 2
        elif(currentWord=='z='):
            word_cnt += 1
            cnt += 2
        else:
            word_cnt += 1
            cnt += 1
    else:
        break

print(word_cnt)


