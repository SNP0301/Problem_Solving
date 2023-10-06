'''
[BOJ] 1158. 요세푸스 문제
T: 2s
M: 256MB

한번 풀고 더 푸는게 1회차
1 + 3번 풀어야 정답처리
'''
import sys
input=sys.stdin.readline

n, k = map(int,input().split())

people = [i for i in range(1,n+1)]
answer_people = list()
## 1 2 3 4 5 6 7: 3
## 4 5 6 7 1 2 : 6
## 7 1 2 4 5
## 4 5 7 1
## 1 4 5
## 1 4
## 4

cnt = n-1
while cnt >= 0:
    if cnt >= k-1:
        answer_people.append(people[k-1])
        people.remove(people[k-1])
        people = people[k-1:] + people[:k-1]
    elif cnt < k-1 and cnt != 0:
        answer_people.append(people[(len(people)%k)//3])
        people.remove(people[(len(people)%k)//3])
        people = people[(len(people)%k)//3:] + people[:(len(people)%k)//3]   
    elif cnt == 0:
        answer_people.append(people[0])
    cnt -= 1


cnt = 0
while cnt < n:
    if cnt == 0:
        print("<%d,"%(answer_people[cnt]),end="")
    elif cnt == n-1:
        print(" %d>"%(answer_people[cnt]),end="")
    else:
        print(" %d,"%(answer_people[cnt]),end="")
    cnt += 1
