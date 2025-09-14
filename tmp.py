"""
긍정

200,000자에 대해 200,000개의 질문
알파벳 26자 배열을 만들어두고 200,000자 쭉 읽어서 누적시키기

200,000 * 26 = 5,200,000

"""
import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)
q = int(input())


pref = [[0]*(n+1) for _ in range(26)]

for i in range(1, n+1):           
    ch = s[i-1]                    
    idx = ord(ch) - 97            
    for c in range(26):
        pref[c][i] = pref[c][i-1] 
    pref[idx][i] += 1             

ans = []

for _ in range(q):
    a, l, r = input().split()
    l = int(l); r = int(r)
    idx = ord(a) - 97
    ans.append(str(pref[idx][r+1] - pref[idx][l]))

sys.stdout.write("\n".join(ans))
