"""

"""

N, M = map(int,input().split())
never_heard = set()
never_seen = set()

for i in range(N):
    never_heard.add(input())

for i in range(M):
    never_seen.add(input())

answer = sorted(list(never_heard.intersection(never_seen)))

print(len(answer))
for i in answer:
    print(i)
