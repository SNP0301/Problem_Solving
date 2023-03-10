word = input()
isPalindrome = 1
for i in range(len(word)//2):
    if(word[i]!=word[len(word)-1-i]):
        isPalindrome = 0

print(isPalindrome)

