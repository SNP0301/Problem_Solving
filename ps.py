'''
[BOJ] 1620. 이모티콘
T: 1초
M: 256MB
'''
import sys
input = sys.stdin.readline

n = int(input())
company = set()

for _ in range(n):
    company_log = input().split()
    if(company_log[1] == 'enter'):
        company.add(company_log[0])
    else:
        company.remove(company_log[0])

company = list(company)
company.sort(reverse=True)

for i in company:
    print(i)