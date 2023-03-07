sentence = input()
sentence += " "
chr_cnt = 0
word_cnt = 0
for i in range(len(sentence)):
    if((ord(sentence[i])>=65)and(sentence[i+1]==" ")):
        word_cnt += 1

print(word_cnt)