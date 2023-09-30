'''
[BOJ] 1181. 단어 정렬 
T: 2초
M: 256MB
'''
import sys
input = sys.stdin.readline

n = int(input())
word_set = set()
for _ in range(n):
    word_set.add(input().rstrip())

word_list = list(word_set)
answer_list = list()

for i in range(len(word_list)):
    answer_list.append([word_list[i],len(word_list[i])])

answer_list.sort(key = lambda x: (x[1],x[0]))

for i in range(len(word_list)):
    print(answer_list[i][0])