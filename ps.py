N = int(input())

members = list()

for i in range(N):
    age, name = input().split()
    members.append([int(age), name])

for person in sorted(members, key = lambda x: x[0]) : ## 가입한 순서로 입력이 주어져서 x[2]가 필요없나?
    print(person[0], person[1])